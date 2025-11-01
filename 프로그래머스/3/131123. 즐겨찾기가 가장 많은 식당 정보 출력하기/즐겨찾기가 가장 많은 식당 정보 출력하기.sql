SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
FROM rest_info r
JOIN (
  SELECT food_type, MAX(favorites) AS max_fav
  FROM rest_info
  GROUP BY food_type
) as m
  ON r.food_type = m.food_type
 AND r.favorites = m.max_fav
ORDER BY r.food_type DESC;
