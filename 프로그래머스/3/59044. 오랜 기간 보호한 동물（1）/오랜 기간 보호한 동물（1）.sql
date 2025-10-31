select I.NAME, I.DATETIME
from ANIMAL_INS as I
where I.ANIMAL_ID not in (
    select O.ANIMAL_ID
    from ANIMAL_OUTS as O
)
order by DATETIME ASC
limit 3;