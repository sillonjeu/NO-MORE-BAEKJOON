select ANIMAL_TYPE, COUNT(ANIMAL_ID) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE = "Dog" ASC