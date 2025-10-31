SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & (1 | 4)) != 0   -- 1 또는 3 보유 (마스크 1+4=5)
  AND (GENOTYPE & 2) = 0;         -- 2 미보유