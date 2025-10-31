select O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS as O
where O.ANIMAL_ID not in (
    select I.ANIMAL_ID
    from ANIMAL_INS as I
)