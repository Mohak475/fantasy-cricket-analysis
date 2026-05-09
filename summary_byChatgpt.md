# Decision Analytics – Fantasy Cricket (IPL 2023)

## Project Overview

This project analyzes fantasy cricket decision-making effectiveness across the IPL 2023 season using manually collected match-level, player-level, and decision-level data.

The analysis evaluates how profitability was influenced by:
- investment behavior,
- player selection quality,
- and Captain/Vice-Captain (C/VC) decisions.

The project was designed as a complete end-to-end analytics workflow involving:
- structured data collection,
- data preparation and validation,
- feature engineering,
- custom metric development,
- benchmarking against optimal outcomes,
- and insight-driven visual analysis.

The work demonstrates strong analytical thinking, decision-system evaluation, and data storytelling using Python, pandas, matplotlib, seaborn, Google Sheets, and marimo notebooks.

---

# Problem Statement

The project investigates the following core question:

> How effective were fantasy cricket decision-making strategies across an entire IPL season?

Three analytical dimensions were explored:

1. **Cost Strategy**
   - Did higher investment improve profitability?
   - Was spending discipline sufficient for better outcomes?

2. **Player Selection Quality**
   - Were high-performing players consistently identified and selected?
   - Were player selections driven by value or behavioral bias?

3. **Captain / Vice-Captain Decisions**
   - Were multiplier decisions aligned with top-performing players?
   - How much scoring potential was left unrealized?

---

# Data System & Pipeline

Data was manually collected throughout IPL 2023 using structured Google Sheets templates designed for:
- efficient match-wise data capture,
- metadata consistency,
- post-match reflection,
- and team selection support.

Three primary datasets were maintained:
- match-level data,
- player-level performance data,
- and team composition / decision data.

The analytical pipeline included:
- dataset export and transformation,
- data cleaning and validation,
- merging player performance with decision data,
- custom metric engineering,
- benchmarking workflows,
- and exploratory visual analysis.

The pipeline was implemented in Python using pandas, matplotlib, seaborn, and marimo notebooks.

---

# Analytical Framework

## Dream Team Benchmarking

Decision quality was benchmarked against the “Dream Team” (DT) for each match — the optimal theoretical team composition based on actual post-match player performance.

This framework enabled:
- evaluation of player selection quality,
- assessment of C/VC effectiveness,
- and measurement of unrealized scoring potential.

For matches with multiple team combinations, only the strongest-performing team was retained for analysis based on overlap with Dream Team points.

---

## Selection Efficiency Index (SEI)

A custom metric — **Selection Efficiency Index (SEI)** — was developed to measure how effectively player points were captured relative to overall player popularity.

The metric combines:
- user selection frequency,
- global selection percentage,
- and percentage of total player points collected.

SEI was used to distinguish between:
- passive alignment with crowd behavior,
- and differentiated high-conviction selections that generated meaningful value.

---

# Key Findings

## 1. Cost Was Not the Primary Driver of Losses

Despite:
- conservative spending across most matches,
- significant mid-season cost reduction,
- and improved spending discipline over time,

overall profitability remained consistently poor.

The analysis showed that:
- average P/L remained negative across all cost ranges,
- and cost reduction alone produced only marginal improvement.

This indicated that:

> selection quality had significantly greater impact on outcomes than investment size.

---

## 2. Player Selection Inefficiency Was Systematic

The project identified repeated inefficiencies in player selection:
- high-performing players were frequently under-selected,
- low-to-moderate performers were repeatedly over-selected,
- and several mid-tier high-value players were consistently ignored.

Selection behavior showed strong evidence of:
- familiarity bias,
- popularity bias,
- and team-level emotional bias.

A major finding was that:

> unrealized value existed primarily among moderately popular but high-performing players.

---

## 3. C/VC Decisions Were a Major Source of Points Leakage

Captain and Vice-Captain selections were identified as one of the largest contributors to underperformance.

Key observations included:
- weak rank alignment with actual top performers,
- poor Vice-Captain decision quality,
- and significant unrealized scoring potential from multiplier choices.

The analysis quantified:
- points left on the table,
- opportunity cost from suboptimal C/VC decisions,
- and the impact of multiplier inefficiency on match outcomes.

---

# Strategic Conclusions

The project concludes that the negative outcomes were not primarily caused by:
- lack of cricket understanding,
- isolated unlucky outcomes,
- or excessive investment.

Instead, the underperformance stemmed from:
- inconsistent decision frameworks,
- bias-driven player selection,
- weak multiplier decision-making,
- and reactive strategic adjustments.

The analysis demonstrates how:

> repeated small decision inefficiencies can compound into persistent long-term underperformance.

---

# Skills Demonstrated

- End-to-end analytics workflow design
- Structured data collection and validation
- Data transformation using pandas
- Feature engineering and custom metric design
- Benchmarking and evaluation framework creation
- Exploratory and statistical analysis
- Behavioral and bias analysis
- Data visualization and analytical storytelling
- Decision-system evaluation

---

# Tech Stack

- Python
- pandas
- matplotlib
- seaborn
- marimo notebooks
- Google Sheets