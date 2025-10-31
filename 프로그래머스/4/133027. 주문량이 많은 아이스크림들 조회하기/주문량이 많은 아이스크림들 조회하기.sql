SELECT f.flavor
FROM first_half AS f
LEFT JOIN (
  SELECT flavor, SUM(total_order) AS july_total
  FROM july
  GROUP BY flavor
) AS j ON j.flavor = f.flavor
ORDER BY (f.total_order + COALESCE(j.july_total, 0)) DESC
LIMIT 3;
