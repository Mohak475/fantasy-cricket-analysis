# Decision Analytics — Fantasy Cricket (IPL 2023)
## Project Summary

---

### Overview

This notebook presents a structured post-season analysis of fantasy cricket decision-making across all 66 matches of the IPL 2023 tournament. The analyst collected match-level, player-level, and team decision data manually through Google Sheets across the full season, then processed and analysed it using Python (Pandas, Matplotlib, Seaborn) in a Marimo reactive notebook environment.

The analysis is structured around three core questions: was the investment strategy efficient, were the right players selected, and were Captain/Vice-Captain (C/VC) multiplier decisions well-calibrated? The Dream Team — the platform's post-match optimal team — is used as the benchmark throughout.

---

### Season at a Glance

- **Total invested:** ₹5,809 across 66 matches
- **Net P/L:** Loss of ₹1,213
- **Profitable matches:** 21% (approximately 14 of 66)
- **Avg cost per match:** ₹88
- **Avg Captain rank:** ~7–8 (1 = ideal)
- **Avg Vice-Captain rank:** ~10–11 (2 = ideal)

---

### Methodology

Three datasets were merged and benchmarked against Dream Team data to evaluate decision quality at each level:

**Match-level analysis** examined cost distribution, weekly spending patterns, and P/L outcomes across the season. Cumulative cost buckets were used to assess whether reducing spend correlated with improved returns.

**Player selection analysis** used the analyst's top team per match — defined as the team with maximum overlap with the Dream Team — to isolate the most informed decisions. A custom metric, the Selection Efficiency Index (SEI), was developed to measure how effectively a player's points were captured relative to their global platform popularity:

$$SEI = \frac{\text{user\_selection\_frequency}}
{\text{global\_selection\%}} \times \frac{\text{points\_earned\%}}{100}$$

**C/VC analysis** benchmarked Captain and Vice-Captain choices against Dream Team assignments using three lenses: DT membership, points rank within the match, and points left on table relative to optimal picks.

---

### Key Findings

**1. Cost management was reactive, not strategic**

Spending was highly volatile in the first three weeks, with average match cost exceeding ₹200 and several matches above ₹300. A sharp 5x cost reduction in week three followed early losses — a reactive correction rather than a planned strategy. The middle phase (weeks 4–8) was the most disciplined, with average cost settling between ₹35–₹70. Despite this correction, average P/L improved by only ~15%, and remained negative across every cost bucket without exception. The data shows clearly that cost management, while necessary, was not the primary driver of outcomes.

**2. Player selection was inverted relative to optimal**

Selection efficiency showed a consistent negative correlation with player quality — the higher a player's total points for the season, the lower the percentage of their points that was captured. Low-performing players (under 200 total points) were selected in nearly every available match, while high-performing players (above 600 total points) were selected inconsistently and captured poorly. The 300–700 total points band — mid-tier players who scored meaningfully across the tournament — represented the largest systematic blind spot. A cluster of players in this range showed near-zero point capture despite high match availability, indicating a strong selection bias against specific players rather than random omission.

The SEI analysis reinforced this pattern. High SEI scores were concentrated among low-performing, low-popularity players — a zone where exceeding the crowd's selection rate had no meaningful impact. Conversely, the high-performance, low-popularity quadrant — where contrarian selection generates the most competitive edge — was largely missed. Selection philosophy appeared to favour familiarity and popularity over match-specific value assessment.

**3. C/VC decisions were the single largest recoverable source of points leakage**

Captain selection showed a partial skill signal — the mode rank was 2, and approximately 24% of matches had the captain ranked 1 or 2. However, the distribution had a long tail extending to rank 24, and a specific over-preference for F du Plessis (captained 7 times against near-zero Dream Team validation) and Suryakumar Yadav (5 times) indicates a clear team-affinity bias distorting otherwise reasonable captain selection logic.

Vice-Captain selection was materially worse. The distribution mode was rank 10 — a full 8 positions below captain — with a near-flat distribution across all ranks suggesting little consistent selection logic. A specific bowler bias was identified: M Siraj selected as VC approximately 5 times and M Shami 4–5 times, both with minimal Dream Team validation. Bowlers have structural scoring ceilings in T20 cricket that make them poor multiplier candidates except in exceptional circumstances. Vice-Captain decisions received demonstrably less analytical rigour than Captain decisions, despite the multiplier impact being only marginally lower (1.5x vs 2x).

**4. Team-level bias compounded individual decision errors**

GT (Gujarat Titans) was the most invested-in team (total cost ~₹1,700) and the worst returning (total P/L ~₹-550). The two largest individual match losses — DC vs GT (₹-215) and PBKS vs GT (₹-185) — were both GT away matches at high cost. This bias was not random; it was systematic and persistent across the tournament. KKR, by contrast, received the lowest total investment and produced the most contained losses — whether by design or by lower match frequency, the result was meaningfully better cost efficiency.

---

### What Worked

- **Mid-tournament cost correction:** The shift to   disciplined, low-cost play in weeks 4–8 reduced   downside exposure and demonstrated that cost   restraint was achievable when applied.

- **CSK match reads:** CSK appeared in three of the   top five most profitable matches. The analyst   showed consistent predictive accuracy for CSK   matchups that was not replicated for other teams.

- **Occasional hidden gem identification:** A small   number of low-popularity, high-performing players   were correctly identified and selected —   confirming that the analytical capability for   contrarian selection exists, even if it was   applied infrequently.

- **Occasional VC outperformance:** Several   Vice-Captain picks generated negative points-on-
  table figures — meaning they outperformed the   Dream Team benchmark. These instances confirm   that genuine VC selection ability exists and   was occasionally deployed.

---

### What Needs to Change

**Priority 1 — C/VC decision framework**
Captain and Vice-Captain decisions should be treated as equally important analytical tasks. A structured pre-match checklist should exclude pure bowlers from the default VC pool, remove team-affinity bias from captain consideration, and use rolling Dream Team validation frequency as a prior for multiplier decisions.

**Priority 2 — Selection recalibration**
Selection philosophy needs to shift from consensus-driven to value-driven. Elite players (projected 600+ total points) should be selected in a minimum percentage of available matches regardless of familiarity. Mid-tier players (300–700 points) should be evaluated on match-
specific conditions rather than rotated by habit. Identifying 2–3 low-popularity, high-potential players before each match should become a deliberate pre-match step.

**Priority 3 — Cost guardrails**
A per-match hard cap — irrespective of conviction level or matchup significance — would have eliminated the two worst losses of the season. The mid-tournament discipline proved this approach is sustainable. It needs to be pre-committed rather than reactively adopted.

**Priority 4 — Bias audit**
Team-level investment limits and player-level familiarity checks should be applied before finalising each team. The GT pattern — high conviction, persistent losses — should serve as the reference case for how unchecked bias compounds over a season.

---

### Technical Note

The notebook is built in Marimo and uses three merged datasets totalling match-level, player-level and decision-level granularity. Key technical components include: C/VC multiplier-adjusted effective points calculation, Dream Team overlap scoring for top team identification, per-match player rank assignment, custom SEI metric derivation, and a suite of Matplotlib/Seaborn visualisations with diverging colour norms, twin axes, secondary x-axes, and adjustText for annotation management.

---


### Skills Demonstrated

**Data Collection & Design**
- Designed and maintained a structured manual data   collection system across a full 66-match tournament   using Google Sheets, covering three levels of   granularity: match, player, and decision
- Defined a consistent benchmarking methodology using   Dream Team data as the post-match optimal baseline

---

**Data Engineering & Transformation (Python / Pandas)**
- Multi-dataset merging across three relational tables   using `pd.merge` with inner and outer joins
- Grouped aggregations using `groupby` with named   aggregation syntax across multiple metrics   simultaneously
- Feature engineering: cumulative columns, date-based   week derivation, cost bucketing with `pd.cut`,   C/VC multiplier application via `.map()` and   `fillna`
- Player rank assignment using `groupby` and   `cumcount` for within-group ordering
- Set-based overlap computation between team   selections and Dream Team using dictionary lookups   and `apply`
- Custom aggregation function using `groupby.apply`   with a named `pd.Series` return for multi-metric   overlap scoring
- Top team identification using `groupby` with   `idxmax` for best-performing team selection   per match
- Boolean filtering, column renaming, `unstack`,   `pivot`, `reset_index` and `fillna` for data   reshaping throughout
- Custom metric design: SEI (Selection Efficiency   Index) — a composite metric combining three   variables into a single interpretable score   with documented methodology and interpretation   guidelines

---

**Data Visualisation (Matplotlib / Seaborn)**
- Histogram with conditional bar coloring based on   value thresholds
- Line charts with dual-variable overlays on shared   and twin y-axes with secondary axis suppression
- Scatter plots with simultaneous encoding of four   variables: x position, y position, color (hue   with diverging norm) and size
- Bar charts with explicit category ordering to   handle non-contiguous discrete axes
- Diverging color normalization using `TwoSlopeNorm`   with semantically meaningful center points
- Dot plot (Cleveland-style) with directional   connecting lines, region shading, bias-colored   y-axis tick labels and secondary x-axis for   long vertical charts
- Heatmaps for team-pair analysis with annotated   values
- Automatic annotation overlap resolution using   `adjustText`
- Consistent visual design system: unified color   palette, font family, background color, spine   styling and chart borders applied across all   figures
- Custom legend construction using   `get_legend_handles_labels` with label   replacement and `Patch` artists for non-standard   legend entries
- Chart export at print resolution (300 DPI) with   `bbox_inches='tight'`

---

**Analytical Thinking**
- Framed a personal dataset as a structured   analytical problem with three independently   measurable dimensions
- Designed a custom metric (SEI) grounded in   domain logic with documented formula,   component interpretation, and known limitations   including low sample size caveats and   comparability validation
- Distinguished between correlated and causally   linked variables — specifically separating   cost management from selection quality as   independent levers
- Identified systematic behavioral patterns   (familiarity bias, team-affinity bias, bowler   VC bias) from quantitative data rather than   subjective recall
- Produced layered analysis: observations →   insights → actionable recommendations at   each section, with a cross-section synthesis   at the conclusion

---

**Notebook & Project Structure**
- Built entirely in Marimo, a reactive Python   notebook framework, with code-hidden cells   for clean presentation
- Structured narrative flow: problem statement →   data overview → preparation → three analysis   sections → conclusions
- Inline observations and insights embedded   alongside each visualisation using `mo.callout`   and `mo.md`
- Summary statistics surfaced at the top of the   notebook using `mo.stat` for executive-level   readability
- Custom CSS integration for font consistency   across Marimo's shadow DOM components
- Dependency management via inline script   metadata compatible with `uv` for reproducible   environment setup
- Visualisations saved to a dedicated `visuals/`   directory at print resolution for portability

---

*The project demonstrates the ability to take a self-defined analytical question from raw data collection through to structured insight delivery — combining technical implementation with domain reasoning and clear communication of findings.*

*This summary was generated from the notebook source file (notebook.py) as an independent review of the project content, structure, and findings.*