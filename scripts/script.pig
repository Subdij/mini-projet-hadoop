-- Chargement des données depuis HDFS
-- Le séparateur est le point-virgule (;)
prenoms = LOAD '/user/maria_dev/ParDepartementDepuis2000.csv' 
         USING PigStorage(';') 
         AS (sexe:int, preusuel:chararray, annais:int, dpt:chararray, nombre:int);

-- Filtrer les lignes anonymisées (_PRENOMS_RARES)
-- On ne garde que les prénoms clairement identifiés
valide = FILTER prenoms BY NOT preusuel MATCHES '_.*';

-- Afficher les données filtrées (valide) dans le terminal
-- À utiliser pour vérification rapide
DUMP valide;