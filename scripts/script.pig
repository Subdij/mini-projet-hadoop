-- Chargement des données depuis HDFS
-- Le séparateur est le point-virgule (;)
prenoms = LOAD '/user/maria_dev/ParDepartementDepuis2000.csv' 
         USING PigStorage(';') 
         AS (sexe:int, preusuel:chararray, annais:int, dpt:chararray, nombre:int);

-- Filtrer les lignes anonymisées et mal formées
valide = FILTER prenoms BY NOT preusuel MATCHES '_.*';

-- Regrouper par prénom, année et sexe (pour additionner les naissances dans différents départements)
groupe_prenom = GROUP valide BY (preusuel, annais, sexe);
somme_par_prenom = FOREACH groupe_prenom GENERATE 
    FLATTEN(group) AS (prenom, annee, sexe), 
    SUM(valide.nombre) AS total_naissances;

-- Regrouper par année et sexe pour organiser les données
groupe_annee_sexe = GROUP somme_par_prenom BY (annee, sexe);

-- Pour chaque groupe (année, sexe), trouver les 5 prénoms les plus fréquents
top_prenoms = FOREACH groupe_annee_sexe {
    -- Trier les prénoms dans chaque groupe par nombre total (décroissant)
    prenoms_tries = ORDER somme_par_prenom BY total_naissances DESC;
    -- Limiter aux 5 premiers
    top5 = LIMIT prenoms_tries 5;
    -- Générer les résultats
    GENERATE 
        group.annee AS annee,
        group.sexe AS sexe,
        top5.(prenom, total_naissances);
}

-- Afficher le résultat
DUMP top_prenoms;