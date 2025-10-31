SELECT
  c.car_id,
  c.car_type,
  FLOOR(c.daily_fee * 30 * (100 - d.discount_rate) / 100) AS fee
FROM car_rental_company_car AS c
JOIN car_rental_company_discount_plan AS d
  ON d.car_type = c.car_type
 AND d.duration_type = '30일 이상'
LEFT JOIN car_rental_company_rental_history AS h
  ON h.car_id = c.car_id
 -- 11월과 겹치는 대여만 매칭
 AND h.start_date <= '2022-11-30'
 AND h.end_date   >= '2022-11-01'
WHERE c.car_type IN ('세단','SUV')
  -- 겹치는 대여가 없으면 h.car_id가 NULL → 대여 가능
  AND h.car_id IS NULL
  -- 30일 요금(정수) 범위 필터
  AND FLOOR(c.daily_fee * 30 * (100 - d.discount_rate) / 100) >= 500000
  AND FLOOR(c.daily_fee * 30 * (100 - d.discount_rate) / 100) < 2000000
ORDER BY fee DESC, c.car_type ASC, c.car_id DESC;