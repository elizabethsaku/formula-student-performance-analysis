-- Table: results (one row per team, FSG 2026). Run via python/load_to_sqlite.py
-- or paste into DB Browser for SQLite / any SQL client after importing the CSV.

-- Q1: reliability. Endurance finishers vs non-finishers
SELECT finished_endurance, COUNT(*) AS teams, ROUND(AVG(total),1) AS avg_total, MAX(total) AS best
FROM results GROUP BY finished_endurance;

-- Q2: static vs dynamic points by tier
SELECT tier, COUNT(*) AS teams, ROUND(AVG(static),1) AS avg_static,
       ROUND(AVG(dynamic),1) AS avg_dynamic, ROUND(AVG(penalty),1) AS avg_penalty
FROM results GROUP BY tier ORDER BY MIN("rank");

-- Q3: Schanzer vs average of ranks 20-30, per discipline
WITH mid AS (
  SELECT AVG(cost) c, AVG(bp) b, AVG(design) d, AVG(accel) a, AVG(skidpad) s, AVG(autox) x
  FROM results WHERE "rank" BETWEEN 20 AND 30)
SELECT 'cost' AS discipline, r.cost AS schanzer, ROUND(m.c,1) AS mid_avg, ROUND(m.c-r.cost,1) AS gap FROM results r, mid m WHERE is_schanzer=1
UNION ALL SELECT 'business plan', r.bp, ROUND(m.b,1), ROUND(m.b-r.bp,1) FROM results r, mid m WHERE is_schanzer=1
UNION ALL SELECT 'design', r.design, ROUND(m.d,1), ROUND(m.d-r.design,1) FROM results r, mid m WHERE is_schanzer=1
UNION ALL SELECT 'acceleration', r.accel, ROUND(m.a,1), ROUND(m.a-r.accel,1) FROM results r, mid m WHERE is_schanzer=1
UNION ALL SELECT 'skidpad', r.skidpad, ROUND(m.s,1), ROUND(m.s-r.skidpad,1) FROM results r, mid m WHERE is_schanzer=1
UNION ALL SELECT 'autocross', r.autox, ROUND(m.x,1), ROUND(m.x-r.autox,1) FROM results r, mid m WHERE is_schanzer=1;

-- Q4: what rank would Schanzer have with +55 points (cost at mid-table level)?
SELECT COUNT(*)+1 AS new_rank FROM results
WHERE total > (SELECT total+55 FROM results WHERE is_schanzer=1);
