WITH q AS (
  SELECT
    id,
    NTILE(4) OVER (ORDER BY size_of_colony DESC, id ASC) AS bucket
  FROM ecoli_data
)
SELECT
  id,
  CASE bucket
    WHEN 1 THEN 'CRITICAL'  -- 상위 0~25%
    WHEN 2 THEN 'HIGH'      -- 26~50%
    WHEN 3 THEN 'MEDIUM'    -- 51~75%
    ELSE 'LOW'              -- 76~100%
  END AS colony_name
FROM q
ORDER BY id;