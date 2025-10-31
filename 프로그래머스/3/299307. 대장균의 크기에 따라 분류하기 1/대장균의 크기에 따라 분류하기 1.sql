select ID, 
CASE
    WHEN SIZE_OF_COLONY <= 100 then "LOW"
    WHEN SIZE_OF_COLONY <= 1000 then "MEDIUM"
    else "HIGH"
END as SIZE
from ECOLI_DATA
order by ID ASC