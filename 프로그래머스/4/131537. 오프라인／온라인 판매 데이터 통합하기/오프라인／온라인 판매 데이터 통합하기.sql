SELECT DATE_FORMAT(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
FROM online_sale
WHERE sales_date >= '2022-03-01' AND sales_date < '2022-04-01'

UNION ALL

SELECT DATE_FORMAT(sales_date, "%Y-%m-%d") as sales_date, product_id, NULL AS user_id, sales_amount
FROM offline_sale
WHERE sales_date >= '2022-03-01' AND sales_date < '2022-04-01'

ORDER BY sales_date ASC, product_id ASC, user_id ASC; 