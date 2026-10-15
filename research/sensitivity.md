# Sensitivity to ratings and weights

Each Monte Carlo view has 20,000 draws with a fixed seed. Score intervals are subjective plausibility ranges, not statistical confidence intervals. High-confidence scores are center-weighted, medium-confidence scores uniform, and low-confidence scores use a random optimistic or pessimistic triangular mode within the declared interval. Weight draws multiply stack shares, workflow dimensions, and stack/workflow balance by declared random factors and renormalize. Win frequencies describe stability of this editorial model only, not objective odds.

## Combined uncertainty

| Environment | Rounded model win frequency | Median rank | Score p10 to p90 |
|---|---:|---:|---:|
| Visual Studio Code | 59% | 1.0 | 8.5 to 8.8 |
| IntelliJ IDEA Ultimate | 41% | 2.0 | 8.5 to 8.7 |
| VSCodium | 0% | 3.0 | 8.2 to 8.4 |
| PyCharm Professional | 0% | 4.0 | 8.2 to 8.4 |
| Neovim | 0% | 5.0 | 7.9 to 8.3 |
| Zed | 0% | 6.0 | 7.6 to 8.1 |
| RustRover | 0% | 7.0 | 7.6 to 7.9 |
| Cursor | 0% | 8.0 | 7.4 to 7.9 |
| Google Antigravity | 0% | 9.0 | 7.3 to 7.8 |
| Devin Desktop | 0% | 10.0 | 7.2 to 7.7 |
| Kiro | 0% | 11.0 | 7.0 to 7.5 |
| Sublime Text 4 | 0% | 12.0 | 6.8 to 7.0 |

## Weights varied, ratings fixed

| Environment | Rounded model win frequency | Median rank | Score p10 to p90 |
|---|---:|---:|---:|
| Visual Studio Code | 88% | 1.0 | 8.6 to 8.7 |
| IntelliJ IDEA Ultimate | 12% | 2.0 | 8.6 to 8.7 |
| VSCodium | 0% | 3.0 | 8.3 to 8.3 |
| PyCharm Professional | 0% | 4.0 | 8.2 to 8.3 |
| Neovim | 0% | 5.0 | 8.0 to 8.1 |
| Zed | 0% | 6.0 | 7.9 to 7.9 |
| RustRover | 0% | 7.0 | 7.7 to 7.8 |
| Cursor | 0% | 8.0 | 7.6 to 7.7 |
| Google Antigravity | 0% | 9.0 | 7.5 to 7.6 |
| Devin Desktop | 0% | 10.0 | 7.4 to 7.5 |
| Kiro | 0% | 11.0 | 7.2 to 7.3 |
| Sublime Text 4 | 0% | 12.0 | 6.8 to 6.9 |

## Ratings varied, weights fixed

| Environment | Rounded model win frequency | Median rank | Score p10 to p90 |
|---|---:|---:|---:|
| Visual Studio Code | 58% | 1.0 | 8.5 to 8.8 |
| IntelliJ IDEA Ultimate | 42% | 2.0 | 8.5 to 8.7 |
| VSCodium | 0% | 3.0 | 8.2 to 8.4 |
| PyCharm Professional | 0% | 4.0 | 8.2 to 8.4 |
| Neovim | 0% | 5.0 | 7.9 to 8.3 |
| Zed | 0% | 6.0 | 7.6 to 8.1 |
| RustRover | 0% | 7.0 | 7.6 to 7.9 |
| Cursor | 0% | 8.0 | 7.4 to 7.9 |
| Google Antigravity | 0% | 9.0 | 7.3 to 7.8 |
| Devin Desktop | 0% | 10.0 | 7.2 to 7.7 |
| Kiro | 0% | 11.0 | 7.1 to 7.5 |
| Sublime Text 4 | 0% | 12.0 | 6.8 to 7.0 |

Interpretation: frequencies depend on subjective ranges, chosen weights, randomization, and seed. They do not estimate user satisfaction or market probability.
