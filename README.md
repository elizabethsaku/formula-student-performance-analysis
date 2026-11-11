# What Separates Top Formula Student Germany Teams? — FSG 2026

An analysis of the official Formula Student Germany (FSG) 2026 overall results, covering **80 teams**, with a performance benchmark of **Schanzer Racing (THI)**.

The project explores which competition events are most associated with overall team performance, how top teams differ from the rest of the field, and where Schanzer Racing has the greatest opportunities to improve.

**Data source:** [Official FSG Results 2026](https://www.formulastudent.de/fsg/results/2026)

## Key Findings

- **Endurance makes a major difference:** Only 28 of 80 teams finished endurance. Finishers averaged approximately 464 points, compared with 228 points for non-finishers. All top-10 teams completed endurance.
- **Top teams excel in dynamic events:** The top 10 averaged approximately 494 dynamic points and 238 static points. Teams ranked 11–30 had a more balanced performance.
- **Autocross has the strongest rank association:** It showed the strongest relationship with final ranking among the events analysed (Spearman's ρ ≈ 0.85).
- **Schanzer Racing's improvement opportunities:** Compared with mid-table teams, the largest approximate point gaps were in Cost (54 points), Business Plan (27), Skidpad (23), and Acceleration (21).

## Tools and Technologies

- **Python:** Data processing and analysis using pandas and SciPy.
- **SQL / SQLite:** Structured data storage and analytical queries.
- **Tableau:**Interactive data visulalization to understand the results.

## Repository Structure

```text
├── data/
│   ├── Cleaned results
│   ├── Enriched results
│   └── Long-format data for BI
├── python/
│   ├── parse.py
│   ├── analyze.py
│   └── load_to_sqlite.py
├── sql/
│   └── 02_analysis.sql
├── powerbi/
│   └── POWERBI_STEPS.md
└── README.md
```

## How to Run

Install the required Python libraries:

```bash
pip install pandas scipy
```

Run the analysis:

```bash
python python/analyze.py
```

Load the data into SQLite:

```bash
python python/load_to_sqlite.py
```

## Limitations

- The analysis covers a single FSG event (2026), so findings may not generalise to other seasons.
- Correlation does not establish causation.
- Dynamic event points contribute to the overall score, so their relationship with final ranking is partly structural.
- Results were transcribed from the official PDF; spot-checking against the original source is recommended.

## Project Objective

The goal is to use data analytics to turn competition results into actionable insights: identifying performance patterns, comparing teams, and highlighting areas where teams can improve.

## Interactive Tableau Dashboard

Explore the FSG 2026 competition results through an interactive Tableau dashboard.

**[View the FSG 2026 Performance Dashboard on Tableau Public](https://public.tableau.com/app/profile/elizabeth.saku/viz/FSG2026FormulaStudentPerformanceAnalysis/FSG2026PerformanceDashboard)**

The dashboard includes:
- Overall team rankings, highlighting Schanzer Racing
- Average static vs. dynamic points by ranking tier
- Endurance completion and average total points
- Autocross performance vs. overall ranking

Interactive filtering allows users to explore performance differences across competition tiers.
