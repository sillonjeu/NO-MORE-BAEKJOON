SELECT d.id, d.email, d.first_name, d.last_name
FROM developers AS d
WHERE (d.skill_code & (
  SELECT SUM(code)           -- 두 스킬 코드의 OR과 같음(코드가 2의 제곱수이므로)
  FROM skillcodes
  WHERE name IN ('Python', 'C#')
)) != 0
ORDER BY d.id;