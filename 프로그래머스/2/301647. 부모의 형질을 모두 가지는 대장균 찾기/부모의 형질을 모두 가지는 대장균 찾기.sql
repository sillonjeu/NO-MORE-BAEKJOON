SELECT
  c.id AS ID,
  c.genotype AS GENOTYPE,
  p.genotype AS PARENT_GENOTYPE
FROM ecoli_data AS c
JOIN ecoli_data AS p
  ON p.id = c.parent_id
WHERE (c.genotype & p.genotype) = p.genotype
ORDER BY c.id ASC;