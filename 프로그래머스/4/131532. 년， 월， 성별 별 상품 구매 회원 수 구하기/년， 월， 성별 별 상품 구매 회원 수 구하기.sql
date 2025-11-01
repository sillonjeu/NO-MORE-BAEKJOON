SELECT
  YEAR(o.sales_date)  AS YEAR,
  MONTH(o.sales_date) AS MONTH,
  u.gender            AS GENDER,
  COUNT(DISTINCT o.user_id) AS USERS
FROM online_sale AS o
JOIN user_info   AS u
  ON u.user_id = o.user_id
WHERE u.gender IS NOT NULL
GROUP BY YEAR(o.sales_date), MONTH(o.sales_date), u.gender
ORDER BY YEAR ASC, MONTH ASC, GENDER ASC;