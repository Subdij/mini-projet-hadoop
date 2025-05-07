#!/usr/bin/env python2
# filepath: c:\Users\ziyad\OneDrive\Bureau\mini-projet-hadoop\python2\post-traitement.py
import sys
import codecs
from collections import defaultdict
import csv
import matplotlib.pyplot as plt
import numpy as np

# Structure pour stocker les donnees: {(annee, sexe): [(prenom, nombre), ...]}
data = defaultdict(list)

output_file = 'resultats.html'
output_graph = 'prenoms_populaires_par_decennie.png'

# Lire les donnees d'entree ligne par ligne
for line in sys.stdin:
    try:
        key, count = line.strip().split('\t')
        year_sex_name = key.split('_')
        if len(year_sex_name) == 3:  # S'assurer que la cle a le bon format
            year, sex, name = year_sex_name
            count = int(count)
            # Stocker le prenom et le nombre dans le groupe correspondant (annee, sexe)
            data[(year, sex)].append((name, count))
    except ValueError:
        # Ignorer les lignes mal formatees
        continue

# Creer le fichier HTML
with codecs.open(output_file, 'w', encoding='utf-8') as htmlfile:
    # Ecrire l'entete HTML avec style CSS
    htmlfile.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Prenoms les plus populaires par annee</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { text-align: center; color: #333; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; cursor: pointer; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:hover { background-color: #f1f1f1; }
        .boys { background-color: #e6f3ff; }
        .girls { background-color: #fff0f5; }
        .year-header { font-weight: bold; background-color: #e0e0e0; }
        #searchInput { margin-bottom: 10px; padding: 8px; width: 250px; }
    </style>
</head>
<body>
    <h1>Prenoms les plus populaires par annee</h1>
    <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Rechercher par annee ou prenom...">
    <table id="resultsTable">
        <thead>
            <tr>
                <th onclick="sortTable(0)">Annee</th>
                <th onclick="sortTable(1)">Sexe</th>
                <th onclick="sortTable(2)">Prenom 1</th>
                <th onclick="sortTable(3)">Nombre</th>
                <th onclick="sortTable(4)">Prenom 2</th>
                <th onclick="sortTable(5)">Nombre</th>
                <th onclick="sortTable(6)">Prenom 3</th>
                <th onclick="sortTable(7)">Nombre</th>
                <th onclick="sortTable(8)">Prenom 4</th>
                <th onclick="sortTable(9)">Nombre</th>
                <th onclick="sortTable(10)">Prenom 5</th>
                <th onclick="sortTable(11)">Nombre</th>
            </tr>
        </thead>
        <tbody>
''')
    
    # Ecrire les donnees dans le tableau
    current_year = None
    for (year, sex), names in sorted(data.items()):
        # Trier les prenoms par nombre (decroissant)
        names.sort(key=lambda x: x[1], reverse=True)
        # Prendre les 5 premiers prenoms (ou moins s'il y en a moins de 5)
        top5 = names[:5]
        
        # Completer avec des valeurs vides si moins de 5 prenoms
        while len(top5) < 5:
            top5.append(("", ""))
        
        # Formater le sexe pour l'affichage
        sex_label = "Filles" if sex == "2" else "Garcons"
        css_class = "girls" if sex == "2" else "boys"
        
        # Ajouter une ligne de separation pour chaque nouvelle annee
        if current_year != year:
            current_year = year
        
        # Ecrire la ligne dans le tableau
        htmlfile.write('        <tr class="{0}">\n'.format(css_class))
        htmlfile.write('            <td>{0}</td>\n'.format(year))
        htmlfile.write('            <td>{0}</td>\n'.format(sex_label))
        
        for name, count in top5:
            htmlfile.write('            <td>{0}</td>\n'.format(name))
            htmlfile.write('            <td>{0}</td>\n'.format(count))
        
        htmlfile.write('        </tr>\n')
    
    # Ecrire le pied du tableau et le JavaScript pour le tri et la recherche
    htmlfile.write('''        </tbody>
    </table>

    <script>
    function sortTable(n) {
        var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
        table = document.getElementById("resultsTable");
        switching = true;
        dir = "asc"; 
        
        while (switching) {
            switching = false;
            rows = table.rows;
            
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[n];
                y = rows[i + 1].getElementsByTagName("TD")[n];
                
                if (dir == "asc") {
                    if (isNaN(x.innerHTML)) {
                        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    } else {
                        if (Number(x.innerHTML) > Number(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                } else if (dir == "desc") {
                    if (isNaN(x.innerHTML)) {
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                            shouldSwitch = true;
                            break;
                        }
                    } else {
                        if (Number(x.innerHTML) < Number(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
            }
            
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                switchcount ++;      
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    }

    function searchTable() {
        var input, filter, table, tr, td, i, j, txtValue, found;
        input = document.getElementById("searchInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("resultsTable");
        tr = table.getElementsByTagName("tr");
        
        for (i = 1; i < tr.length; i++) {
            found = false;
            td = tr[i].getElementsByTagName("td");
            
            for (j = 0; j < td.length; j++) {
                if (td[j]) {
                    txtValue = td[j].textContent || td[j].innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }
            
            if (found) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
    </script>
</body>
</html>''')

# Organiser les donnees par decennies
data_by_decade = defaultdict(lambda: defaultdict(int))

for (year, sex), names in data.items():
    # Calculer la decennie (ex: 1900, 1910, 1920...)
    decade = int(year) // 10 * 10
    decade_label = "{0}s".format(decade)
    
    for name, count in names:
        if name:  # Ne pas prendre en compte les valeurs vides
            data_by_decade[(decade_label, sex)][name] += count

# Trouver le prenom le plus populaire pour chaque decennie et sexe
top_names_by_decade = {}

# Liste pour garder l'ordre des decennies
all_decades = sorted(set(decade for (decade, _) in data_by_decade.keys()))

for decade in all_decades:
    top_names_by_decade[decade] = {}
    
    # Pour les garcons (sexe = "1")
    if (decade, "1") in data_by_decade:
        boys_names = data_by_decade[(decade, "1")]
        if boys_names:
            top_boy_name = max(boys_names.items(), key=lambda x: x[1])
            top_names_by_decade[decade]["1"] = top_boy_name
    
    # Pour les filles (sexe = "2")
    if (decade, "2") in data_by_decade:
        girls_names = data_by_decade[(decade, "2")]
        if girls_names:
            top_girl_name = max(girls_names.items(), key=lambda x: x[1])
            top_names_by_decade[decade]["2"] = top_girl_name

# Preparer les donnees pour le graphique en barres
decades = []
top_boys_names = []
boys_counts = []
top_girls_names = []
girls_counts = []

for decade in all_decades:
    decades.append(decade)
    
    # Recuperer le prenom le plus populaire des garcons et son nombre
    if "1" in top_names_by_decade[decade]:
        name, count = top_names_by_decade[decade]["1"]
        top_boys_names.append(name)
        boys_counts.append(count)
    else:
        top_boys_names.append("")
        boys_counts.append(0)
    
    # Recuperer le prenom le plus populaire des filles et son nombre
    if "2" in top_names_by_decade[decade]:
        name, count = top_names_by_decade[decade]["2"]
        top_girls_names.append(name)
        girls_counts.append(count)
    else:
        top_girls_names.append("")
        girls_counts.append(0)

# Creer le graphique en barres
plt.figure(figsize=(14, 8))

# Parametres pour les barres
x = np.arange(len(decades))
width = 0.35

# Creer les barres
bars1 = plt.bar(x - width/2, boys_counts, width, label='Garcons', color='cornflowerblue')
bars2 = plt.bar(x + width/2, girls_counts, width, label='Filles', color='lightpink')

# Ajouter les etiquettes, le titre et les legendes
plt.xlabel('Decennie', fontsize=12)
plt.ylabel('Nombre d\'attributions', fontsize=12)
plt.title('Prenom le plus populaire par decennie et par sexe', fontsize=16)
plt.xticks(x, decades)
plt.legend()

# Ajouter les noms des prenoms au-dessus des barres
def add_labels(bars, names):
    for i, (bar, name) in enumerate(zip(bars, names)):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                name, ha='center', va='bottom', rotation=45, fontsize=9)

add_labels(bars1, top_boys_names)
add_labels(bars2, top_girls_names)

# Ajuster la mise en page
plt.tight_layout()

# Sauvegarder le graphique
plt.savefig(output_graph, dpi=300, bbox_inches='tight')

print "Les resultats ont ete ecrits dans le fichier %s" % output_file
print "Le graphique des prenoms les plus populaires par decennie a ete sauvegarde dans %s" % output_graph

