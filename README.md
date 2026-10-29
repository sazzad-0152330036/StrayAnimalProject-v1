# Stray Animal Welfare Intelligence – Bangladesh (V1)

**A news-based stray animal welfare risk analysis and visualization project focused on Bangladesh.**

## Overview

This project explores how publicly available news reports can be organized and analyzed to identify patterns in stray animal welfare incidents in Bangladesh. Version 1 (V1) focuses on **web scraping, data wrangling, a rule-based risk index, and exploratory visualizations** rather than machine-learning prediction.

## Objectives

- Collect news reports relevant to stray animals in Bangladesh.
- Clean, filter, and structure the collected news records.
- Categorize reports by animal type and incident type.
- Assign interpretable risk scores and risk levels using a **Stray Animal Risk Index (SARI)** approach.
- Explore incident patterns, source contributions, trends, and geographic distribution through visualizations.

## Project Workflow

```text
News search / web scraping
           |
           v
Raw news records (~250)
           |
           v
Cleaning and relevance filtering
           |
           v
Filtered news records (~190)
           |
           v
Animal / incident categorization
           |
           v
SARI risk scoring and risk levels
           |
           v
Exploratory analysis and visualizations
```

## Dataset

The V1 workflow began with approximately **250 collected news records**, reduced to approximately **190 records** after filtering. Reported fields include:

| Field | Meaning |
| --- | --- |
| `keyword` | Search keyword used to find the report |
| `title` | News article headline |
| `link` | Source URL |
| `summary` | Article summary or extracted description |
| `date` | Publication date, when available |
| `animal_type` | Animal category associated with the report |
| `incident_type` | Categorized welfare-related incident |

**Data note:** These figures describe the earlier V1 workflow. Exact record counts, column names, and scraping sources should be checked against the files in this repository before treating them as final.

## Stray Animal Risk Index (SARI)

SARI is a **rule-based risk assessment component** used to convert categorized news incidents into:

- `risk_score` — a numeric indicator assigned according to the project's scoring rules.
- `risk_level` — a categorical interpretation of the score.

The purpose is to support **relative prioritization and interpretation** of reported incidents. It is **not** a validated measure of actual animal suffering, population risk, or incident prevalence. News coverage can be incomplete or uneven across regions.

> **Implementation note:** The precise scoring weights, thresholds, and risk-level labels should be documented from the original V1 code. They are intentionally not invented here.

## Analysis and Visualizations

The V1 work includes exploratory outputs relating to:

- Distribution of incident categories and animal types
- SARI risk scores and levels
- News source contributions
- Changes in news-report trends over time
- Geographic or map-based summaries where location information is available

These outputs describe patterns **in the collected news dataset**, not a complete census of stray animal incidents across Bangladesh.

## Tools and Methods

- **Python** — data collection, transformation, analysis, and reporting
- **Web scraping / news collection** — assembling the source records
- **Data wrangling** — cleaning, filtering, and structuring records
- **Rule-based scoring (SARI)** — interpretable incident-risk categorization
- **Data visualization** — trends, distributions, and geographic summaries

*Specific Python packages and exact commands should be added after checking the original V1 source files.*

## Project Scope

**V1:** News-based data collection, cleaning, categorization, SARI scoring, and exploratory visualization.

**V2 (separate extension):** Machine-learning experiments and further welfare-intelligence analysis. V2 results and model performance are not claimed as part of this V1 repository.

## Limitations

1. News coverage may be biased toward highly reported locations or incidents.
2. Search terms, news availability, and filtering rules affect which records are included.
3. Incident labels and rule-based scores depend on the chosen categorization and scoring logic.
4. The dataset may not represent the true frequency or severity of stray animal welfare problems.
5. This version is primarily exploratory; it does not establish causal relationships or provide validated predictions.

## Repository Contents

Place the original V1 scripts, data, figures, and report in this repository. A possible organization is:

```text
Stray-Animal-Welfare-Intelligence-V1/
├── README.md
├── data/              # Collected and processed datasets (if available)
├── src/               # Scraping, cleaning, scoring, analysis scripts
├── figures/           # Exported plots and maps
└── reports/           # Project report or documentation
```

This is a **suggested structure**, not a claim about the names of existing files. Keep the actual project folders if they are already organized differently.

## How to Run

The exact setup and run commands depend on the original V1 code and dependencies. After adding those files, document:

1. Python version and required packages.
2. Input dataset location and format.
3. Script or notebook execution order.
4. How to regenerate the figures and report.

Avoid committing credentials, private API keys, or copyrighted full-text news articles without permission.

## Future Work

Potential extensions include richer incident extraction, geographic hotspot analysis, additional data sources, and machine-learning-based analysis. These are **future directions**, not features asserted to be implemented in V1.

---

**Project:** Stray Animal Welfare Intelligence – Bangladesh  
**Version:** V1  
**Focus:** News Data Wrangling · SARI Risk Analysis · Exploratory Visualization
