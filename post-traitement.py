import sys
from collections import defaultdict
import csv

# Structure pour stocker les données: {(année, sexe): [(prénom, nombre), ...]}
data = defaultdict(list)

output_file = 'resultats.html'

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

# Créer le fichier HTML
with open(output_file, 'w', encoding='utf-8') as htmlfile:
    # Écrire l'entête HTML avec style CSS
    htmlfile.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Prénoms les plus populaires par année</title>
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
    <h1>Prénoms les plus populaires par année</h1>
    <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="Rechercher par année ou prénom...">
    <table id="resultsTable">
        <thead>
            <tr>
                <th onclick="sortTable(0)">Année</th>
                <th onclick="sortTable(1)">Sexe</th>
                <th onclick="sortTable(2)">Prénom 1</th>
                <th onclick="sortTable(3)">Nombre</th>
                <th onclick="sortTable(4)">Prénom 2</th>
                <th onclick="sortTable(5)">Nombre</th>
                <th onclick="sortTable(6)">Prénom 3</th>
                <th onclick="sortTable(7)">Nombre</th>
                <th onclick="sortTable(8)">Prénom 4</th>
                <th onclick="sortTable(9)">Nombre</th>
                <th onclick="sortTable(10)">Prénom 5</th>
                <th onclick="sortTable(11)">Nombre</th>
            </tr>
        </thead>
        <tbody>
''')
    
    # Écrire les données dans le tableau
    current_year = None
    for (year, sex), names in sorted(data.items()):
        # Trier les prénoms par nombre (décroissant)
        names.sort(key=lambda x: x[1], reverse=True)
        # Prendre les 5 premiers prénoms (ou moins s'il y en a moins de 5)
        top5 = names[:5]
        
        # Compléter avec des valeurs vides si moins de 5 prénoms
        while len(top5) < 5:
            top5.append(("", ""))
        
        # Formater le sexe pour l'affichage
        sex_label = "Filles" if sex == "2" else "Garçons"
        css_class = "girls" if sex == "2" else "boys"
        
        # Ajouter une ligne de séparation pour chaque nouvelle année
        if current_year != year:
            current_year = year
        
        # Écrire la ligne dans le tableau
        htmlfile.write(f'        <tr class="{css_class}">\n')
        htmlfile.write(f'            <td>{year}</td>\n')
        htmlfile.write(f'            <td>{sex_label}</td>\n')
        
        for name, count in top5:
            htmlfile.write(f'            <td>{name}</td>\n')
            htmlfile.write(f'            <td>{count}</td>\n')
        
        htmlfile.write('        </tr>\n')
    
    # Écrire le pied du tableau et le JavaScript pour le tri et la recherche
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

print(f"Les résultats ont été écrits dans le fichier {output_file}")

