from pathlib import Path
import json
import random
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "research" / "model-results.json"
criteria = json.loads((DATA / "criteria.json").read_text(encoding="utf-8"))
environments = json.loads((DATA / "environments.json").read_text(encoding="utf-8"))
scenarios = json.loads((DATA / "scenarios.json").read_text(encoding="utf-8"))
ids = [item["id"] for item in criteria]

def parsed(candidate):
    values = {}
    for key, value in zip(ids, candidate["scores"].split(","), strict=True):
        low, high = (float(part) for part in value.split("-"))
        values[key] = (low, high)
    return values

RATINGS = {candidate["id"]: parsed(candidate) for candidate in environments}
CONFIDENCE = {candidate["id"]: candidate.get("confidence", {}) for candidate in environments}

def stack_range(values, mix):
    result = [0.0, 0.0]
    for key, share in mix.items():
        bounds = [statistics.mean([values[k][i] for k in ("rust", "web", "python")]) for i in (0, 1)] if key == "other" else values[key]
        for i in (0, 1):
            result[i] += bounds[i] * share / 100.0
    return tuple(result)

def dimension_range(values, weights):
    total = sum(weights.values()) or 1
    return tuple(sum(values[key][i] * weight for key, weight in weights.items()) / total for i in (0, 1))

def score_range(values, scenario):
    stack = stack_range(values, scenario["stack"])
    dims = dimension_range(values, scenario["dimensions"])
    stack_weight = scenario.get("stack_weight", 55) / 100
    return tuple(stack_weight * stack[i] + (1-stack_weight) * dims[i] for i in (0, 1))

def midpoint(value):
    return (value[0] + value[1]) / 2

def evaluate(values, scenario):
    scored = [(candidate, score_range(values[candidate["id"]], scenario)) for candidate in environments]
    return sorted(scored, key=lambda row: midpoint(row[1]), reverse=True)

def draw_ratings(rng):
    drawn = {}
    for cid, record in RATINGS.items():
        drawn[cid] = {}
        for key, (low, high) in record.items():
            level = CONFIDENCE[cid].get(key, "medium")
            middle = (low + high) / 2
            if level == "high":
                sample = rng.triangular(low, high, middle)
            elif level == "low":
                # Low-confidence scores explore both optimistic and pessimistic tails.
                mode = low if rng.getrandbits(1) == 0 else high
                sample = rng.triangular(low, high, mode)
            else:
                sample = rng.uniform(low, high)
            drawn[cid][key] = (sample, sample)
    return drawn

def varied_weights(rng, weights, amount=.20):
    raw = {key: value * rng.uniform(1-amount, 1+amount) for key, value in weights.items()}
    total = sum(raw.values()) or 1
    return {key: value*100/total for key, value in raw.items()}

def varied_scenario(rng, scenario):
    return {"stack":varied_weights(rng,scenario["stack"]),"dimensions":varied_weights(rng,scenario["dimensions"]),
            "stack_weight":max(20,min(80,rng.uniform(scenario.get("stack_weight",55)-5,scenario.get("stack_weight",55)+5)))}

def simulation(scenario, mode, trials=20000, seed=20261015):
    rng = random.Random(seed + sum(ord(c) for c in scenario["id"]) + len(mode))
    scores_by_id = {c["id"]:[] for c in environments}
    ranks_by_id = {c["id"]:[] for c in environments}
    wins = {c["id"]:0 for c in environments}
    for _ in range(trials):
        values = draw_ratings(rng) if mode in ("ratings","combined") else RATINGS
        current = varied_scenario(rng,scenario) if mode in ("weights","combined") else scenario
        ranked = sorted(((c,score_range(values[c["id"]],current)) for c in environments),key=lambda row:midpoint(row[1]),reverse=True)
        wins[ranked[0][0]["id"]] += 1
        for rank,(candidate,bound) in enumerate(ranked,1):
            cid=candidate["id"]
            scores_by_id[cid].append(midpoint(bound))
            ranks_by_id[cid].append(rank)
    result={}
    for candidate in environments:
        cid=candidate["id"]; samples=sorted(scores_by_id[cid])
        result[cid]={"win_frequency_percent_rounded":round(100*wins[cid]/trials),
                     "median_rank":round(statistics.median(ranks_by_id[cid]),1),
                     "score_p10_p90":[round(samples[int(trials*.10)],1),round(samples[min(trials-1,int(trials*.90))],1)]}
    return {"trials":trials,"frequency_is_model_stability_not_market_probability":True,"candidates":result}

def main():
    scenario_results={}
    for scenario in scenarios:
        ranking=evaluate(RATINGS,scenario)
        scenario_results[scenario["id"]]={"winner":ranking[0][0]["id"],"runner_up":ranking[1][0]["id"],
          "winner_range":[round(x,1) for x in ranking[0][1]],"runner_up_range":[round(x,1) for x in ranking[1][1]],
          "overlap":ranking[0][1][0]<=ranking[1][1][1]}
    balanced=next(s for s in scenarios if s["id"]=="balanced")
    sensitivity={mode:simulation(balanced,mode) for mode in ("weights","ratings","combined")}
    result={"generated_on":"2026-10-15","model":"27 scored criteria, scenario-specific stack share, and 23 direct-duel dimensions",
      "scores_are_editorial_ranges_not_measurements":True,
      "sensitivity_interpretation":"High-confidence draws are center-weighted; medium-confidence draws are uniform; low-confidence draws use a random optimistic or pessimistic triangular mode within the editorial interval. Monte Carlo frequencies show stability of this chosen model only; they are not objective probabilities.",
      "scenario_results":scenario_results,"balanced_sensitivity":sensitivity}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    if "--summary" in sys.argv:
        print(json.dumps({"scenarios":scenario_results,"combined":sensitivity["combined"]},indent=2))

if __name__ == "__main__":
    main()
