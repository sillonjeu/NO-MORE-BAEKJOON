SELECT
  e1.id AS ID,
  COUNT(e2.id) AS CHILD_COUNT
FROM ecoli_data AS e1
LEFT JOIN ecoli_data AS e2
  ON e2.parent_id = e1.id     -- 부모의 ID = 자식의 PARENT_ID
GROUP BY e1.id
ORDER BY e1.id ASC;