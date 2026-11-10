# Power BI dashboard (build in ~30 min)
Power BI Desktop is Windows-only (free). On Mac, use Power BI Service in the browser or Tableau Public.

## 1. Load data
Home > Get data > Text/CSV:
- `data/fsg26_results_enriched.csv` -> table **results**
- `data/fsg26_points_long.csv` -> table **points_long**
Relationship: results[team] 1 -> * points_long[team] (Model view).

## 2. DAX measures (Modeling > New measure)
```
Teams = COUNTROWS(results)
Avg Total = AVERAGE(results[total])
Endurance Finish % = DIVIDE(SUM(results[finished_endurance]), COUNTROWS(results))
Avg Static = AVERAGE(results[static])
Avg Dynamic = AVERAGE(results[dynamic])
Schanzer Rank = CALCULATE(MAX(results[rank]), results[is_schanzer] = 1)
Gap to Mid-table =
VAR mid = CALCULATE(AVERAGE(points_long[points]), FILTER(ALL(results), results[rank] >= 20 && results[rank] <= 30))
VAR sch = CALCULATE(AVERAGE(points_long[points]), results[is_schanzer] = 1)
RETURN mid - sch
```

## 3. Pages / visuals
1. **Overview**: cards (Teams, Endurance Finish %, Schanzer Rank); bar chart tier vs Avg Static / Avg Dynamic (clustered); slicer on country.
2. **Reliability**: column chart finished_endurance vs Avg Total; scatter rank (X) vs total (Y), legend = finished_endurance.
3. **Schanzer**: clustered bar, axis = points_long[discipline], values = Avg points, legend = tier; plus Gap to Mid-table by discipline.
Conditional formatting: highlight is_schanzer = 1 in a table visual.

## 4. Publish
Save as `powerbi/fsg_dashboard.pbix`, export 2-3 screenshots to `powerbi/screenshots/` and embed them in the main README.
