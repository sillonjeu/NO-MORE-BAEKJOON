select I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
from ANIMAL_INS as I join ANIMAL_OUTS as O
on I.ANIMAL_ID = O.ANIMAL_ID
where I.SEX_UPON_INTAKE like "Intact %" 
  AND (
        O.SEX_UPON_OUTCOME LIKE 'Spayed %'
     OR O.SEX_UPON_OUTCOME LIKE 'Neutered %'
      );