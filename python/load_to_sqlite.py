"""Load the CSV into a SQLite database, then run sql/02_analysis.sql."""
import sqlite3, pandas as pd, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
con = sqlite3.connect(root / "fsg.db")
pd.read_csv(root / "data/fsg26_results_enriched.csv").to_sql("results", con, if_exists="replace", index=False)
sql = (root / "sql/02_analysis.sql").read_text()
for i, stmt in enumerate([s for s in sql.split(";") if "SELECT" in s.upper()], 1):
    print(f"--- query {i} ---")
    print(pd.read_sql_query(stmt, con).to_string(index=False))
con.close()
