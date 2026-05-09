# Fantasy Sports Decision Analytics — IPL 2023

A structured post-season analysis of fantasy cricket decision-making across all 66 matches of the IPL 2023 tournament. The project evaluates investment behavior, player selection quality, and Captain/Vice-Captain (C/VC) multiplier decisions against the platform's post-match optimal team (Dream Team), and identifies the systematic decision errors driving persistent underperformance.

---

## Problem Statement

> How effective were my fantasy cricket decision-making strategies across an entire IPL season?

Three analytical dimensions were investigated:

1. **Cost strategy** — Did higher investment improve returns? Was spending discipline sufficient?
2. **Player selection** — Were high-performing players consistently identified and selected, or was selection driven by bias?
3. **C/VC decisions** — Were multiplier choices aligned with top performers? How much scoring potential was left unrealised?

---

## Season at a Glance

| Metric | Value |
|--------|-------|
| Matches played | 66 |
| Total invested | ₹5,809 |
| Net P/L | −₹1,213 |
| Profitable matches | ~21% |
| Avg cost per match | ₹88 |
| Avg Captain rank | ~7–8 (1 = ideal) |
| Avg Vice-Captain rank | ~10–11 (2 = ideal) |

---

## Methodology

### Dream Team Benchmarking

Every decision was evaluated against the **Dream Team (DT)** — the platform's post-match optimal team based on actual player performance. This benchmark enabled objective measurement of selection quality and C/VC effectiveness, independent of match outcomes.

For matches with multiple submitted team compositions, only the top-performing team (highest DT overlap score) was retained for player-level analysis.

### Selection Efficiency Index (SEI)

A custom metric was developed to distinguish genuine contrarian value from passive crowd-following:

$$SEI = \frac{\text{user\_selection\_frequency}}{\text{global\_selection\%}} \times \frac{\text{points\_earned\%}}{100}$$

A high SEI in a low-performance, low-popularity zone indicates wasted contrarian effort. A high SEI in the high-performance, low-popularity zone indicates genuine competitive edge. The metric was used to map selection patterns across both dimensions simultaneously.

---

## Key Findings

### 1. Cost management was reactive, not strategic

Spending was highly volatile in the first three weeks (avg cost > ₹200/match, several exceeding ₹300). A sharp reduction followed early losses — a reactive correction rather than a planned approach. Despite improved discipline in weeks 4–8, average P/L remained negative across every cost bucket. Cost management was necessary but not the primary driver of outcomes.

### 2. Player selection was inverted relative to optimal

The higher a player's total season points, the lower the percentage of their points that was captured. Low-performing players were selected in almost every available match; high-performing players were selected inconsistently. The 300–700 total-points band — mid-tier players who scored meaningfully across the tournament — represented the largest systematic blind spot. Selection favoured familiarity and platform popularity over match-specific value.

### 3. C/VC decisions were the largest recoverable source of points leakage

Captain selection showed a partial skill signal (mode rank = 2; ~24% of matches with rank 1 or 2) but was distorted by team-affinity bias — F du Plessis captained 7 times with near-zero Dream Team validation. Vice-Captain selection was materially worse (mode rank = 10), with a near-flat rank distribution indicating little consistent logic. A specific bowler bias (M Siraj ~5× VC, M Shami ~4–5× VC) compounded underperformance given structural T20 scoring ceilings for bowlers.

---

## Data

Data was collected manually throughout IPL 2023 using structured Google Sheets templates, then exported as three CSV files:

| File | Granularity | Key fields |
|------|-------------|------------|
| `data/dataset1_export.csv` | One row per match | Cost, winnings, net P/L, team count |
| `data/dataset2_export.csv` | One row per player per match | Fantasy points, global selection %, role, team |
| `data/dataset3_export.csv` | One row per player per team per match | Selected players, C/VC assignments, Dream Team flags |

---

## Visualisations

Thirteen charts are saved at 300 DPI in the `visuals/` directory, covering:

- P/L and cost distributions (`pl_distribution.png`, `cost_histogram.png`)
- Weekly spending trends (`weekly_avg_cost.png`)
- Cumulative cost vs cumulative P/L (`cumulative_cost_pl.png`)
- Team-level cost and P/L breakdown (`teamwise_cost_pl.png`)
- Points captured vs total points scatter (`points_captured_scatter.png`)
- Selection Efficiency Index scatter (`sei_scatter.png`)
- C/VC rank distributions (`cvc_rank_distribution.png`)
- Captain and Vice-Captain player-level comparison dot plots (`player_level_c_comparison.png`, `player_level_vc_comparison.png`)
- Points on table vs rank (`points_on_table_vs_rank.png`)
- Role-wise C/VC preference (`rolewise_cvc_preference.png`)
- Cost vs P/L scatter (`cost_vs_pl.png`)
- Team-pair heatmaps (`team_pair_heatmaps.png`)

---

## Project Structure

```
fantasy-cricket-analysis/
├── ipl2023.py               # Marimo reactive notebook (main analysis)
├── data/
│   ├── dataset1_export.csv  # Match-level data
│   ├── dataset2_export.csv  # Player-level data
│   └── dataset3_export.csv  # Decision/composition data
├── visuals/                 # All exported charts (300 DPI PNG)
├── summary_byClaude.md      # Detailed project summary (Claude)
├── summary_byChatgpt.md     # Detailed project summary (ChatGPT)
└── pyproject.toml           # Project dependencies (uv)
```

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Notebook environment | [Marimo](https://marimo.io/) |
| Data manipulation | pandas, NumPy |
| Visualisation | Matplotlib, Seaborn, adjustText |
| Dependency management | [uv](https://github.com/astral-sh/uv) |
| Data collection | Google Sheets |
| Language | Python 3.13 |

---

## Skills Demonstrated

**Data collection & design**
- Designed and maintained a structured manual data collection system across a full 66-match tournament at three levels of granularity (match, player, decision)
- Defined a consistent benchmarking methodology using Dream Team data as the post-match optimal baseline

**Data engineering (Python / pandas)**
- Multi-dataset merging across three relational tables using inner and outer joins
- Feature engineering: cumulative columns, week derivation from dates, cost bucketing with `pd.cut`, C/VC multiplier application
- Custom metric design: SEI — a composite metric combining selection frequency, platform popularity, and points capture with documented formula and interpretation guidelines
- Set-based Dream Team overlap scoring, `groupby.apply` with multi-metric named Series returns, `pivot`, `unstack`, and boolean filtering throughout

**Visualisation (Matplotlib / Seaborn)**
- Diverging color normalization with `TwoSlopeNorm` for semantically meaningful charts
- Scatter plots encoding four simultaneous variables (position × 2, hue, size)
- Cleveland-style dot plots with directional connectors, region shading, and bias-colored axis labels
- Dual y-axis and secondary x-axis charts, heatmaps, and conditional bar coloring
- Automatic annotation overlap resolution using `adjustText`
- Consistent visual design system applied across all 13 figures; exported at 300 DPI

**Analytical thinking**
- Framed a personal dataset as a structured analytical problem with three independently measurable dimensions
- Separated correlated variables (cost vs selection quality) as independent causal levers
- Identified systematic behavioral patterns (familiarity bias, team-affinity bias, bowler VC bias) from quantitative data rather than subjective recall
- Produced layered analysis: observations → insights → actionable recommendations at each section

---

*This project demonstrates the ability to take a self-defined analytical question from raw data collection through to structured insight delivery — combining technical implementation with domain reasoning and clear communication of findings.*

---

*This README was generated with the assistance of AI (Claude by Anthropic).*
