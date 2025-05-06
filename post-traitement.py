import sys
from collections import defaultdict

# Structure pour stocker les données: {(année, sexe): [(prénom, nombre), ...]}
data = defaultdict(list)

# Lire les données d'entrée ligne par ligne
for line in sys.stdin:
    try:
        key, count = line.strip().split('\t')
        year_sex_name = key.split('_')
        if len(year_sex_name) == 3:  # S'assurer que la clé a le bon format
            year, sex, name = year_sex_name
            count = int(count)
            # Stocker le prénom et le nombre dans le groupe correspondant (année, sexe)
            data[(year, sex)].append((name, count))
    except ValueError:
        # Ignorer les lignes mal formatées
        continue

# Pour chaque groupe (année, sexe), trouver les 5 prénoms les plus fréquents
for (year, sex), names in sorted(data.items()):
    # Trier les prénoms par nombre (décroissant)
    names.sort(key=lambda x: x[1], reverse=True)
    # Prendre les 5 premiers prénoms (ou moins s'il y en a moins de 5)
    top5 = names[:5]
    
    # Formater les résultats
    sex_label = "Filles" if sex == "2" else "Garçons"
    print(f"Année {year}, {sex_label}:")
    
    # Afficher les prénoms et leurs nombres
    for i, (name, count) in enumerate(top5, 1):
        print(f"  {i}. {name}: {count}")
    
    print()  # Ligne vide pour séparer les groupes

