# What separates top Formula Student Germany teams? (FSG 2026)

Analysis of the official FSG 2026 overall results (80 teams) with a benchmark of Schanzer Racing (THI).
Source: official results PDF, formulastudent.de/fsg/results/2026

## Key findings
- Only 28/80 teams finished endurance; finishers averaged ~464 points vs ~228 for non-finishers. All top-10 teams finished.
- Top-10 teams average ~494 dynamic vs ~238 static points; teams ranked 11-30 are roughly balanced.
- Autocross is the strongest single predictor of final rank (Spearman rho 0.85).
- Schanzer: largest gaps to mid-table are cost (~54 pts), business plan (~27), skidpad (~23), acceleration (~21).

## Structure
- `data/` cleaned results (wide, enriched, long format for BI)
- `python/` parsing, analysis (pandas/scipy), SQLite loader
- `sql/` analysis queries
- `powerbi/` dashboard build steps and DAX

## Run
```
pip install pandas scipy
python python/analyze.py
python python/load_to_sqlite.py
```

## Limitations
Single event; association not causation; transcribed from PDF (spot-check recommended). Dynamic points are part of the total, so their correlation with rank is partly structural.
