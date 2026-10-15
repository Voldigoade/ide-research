const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const root = path.resolve(__dirname, "..");
const read = name => JSON.parse(fs.readFileSync(path.join(root, name), "utf8"));

test("structured catalog has unique IDs and complete score vectors", () => {
  const criteria = read("data/criteria.json");
  const products = read("data/environments.json");
  assert.equal(new Set(criteria.map(x=>x.id)).size, criteria.length);
  assert.equal(new Set(products.map(x=>x.id)).size, products.length);
  for (const product of products) {
    const values = product.scores.split(",");
    assert.equal(values.length, criteria.length, product.id);
    for (const value of values) {
      const [low, high] = value.split("-").map(Number);
      assert.ok(low >= 1 && high <= 10 && low <= high, product.id + " " + value);
    }
  }
});

test("scenario stack mixes are explicit and total 100 percent", () => {
  const scenarios = read("data/scenarios.json");
  assert.equal(scenarios.length, 10);
  for (const scenario of scenarios) {
    assert.equal(Object.values(scenario.stack).reduce((a,b)=>a+b,0), 100, scenario.id);
  }
  const rust = scenarios.find(x=>x.id==="rust");
  assert.ok(rust.stack.rust > 50);
  assert.ok(rust.stack.tauri > rust.stack.web);
});

test("sources referenced by finalists exist", () => {
  const sources = read("data/sources.json");
  const known = new Set(sources.map(x=>x.id));
  for (const product of read("data/environments.json")) {
    for (const id of product.sources) assert.ok(known.has(id), product.id + ": " + id);
  }
});
