import csv
import os

def validate_csv():
    input_file = 'nat2022.csv'
    output_file = 'nat2022_valid.csv'
    
    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_file):
        print(f"Erreur: Le fichier {input_file} n'existe pas.")
        return
    
    total_lines = 0
    valid_lines = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            
            # Créer le lecteur et l'écrivain CSV
            reader = csv.reader(infile, delimiter=';')
            writer = csv.writer(outfile, delimiter=';')
            
            # Ignorer l'en-tête
            header = next(reader, None)
            
            # Écrire l'en-tête dans le fichier de sortie (optionnel)
            if header:
                writer.writerow(header)
            
            # Traiter chaque ligne
            for row in reader:
                total_lines += 1
                
                # Vérifier que la ligne a exactement 5 champs
                if len(row) != 5:
                    continue
                
                # Vérifier que les champs requis ne sont pas vides
                sexe, preusuel,annais,dept, nombre= row
                if not annais or not sexe or not nombre or not dept:
                    continue
                
                # Vérifier que le prenom est valide (différent de "_PRENOMS_RARES")
                if preusuel == "_PRENOMS_RARES":
                    continue
                
                # Vérifer que le sexe est valide (1 ou 2)
                if sexe not in ['1', '2']:
                    continue
                
                # Vérifier que le département est valide (2 chiffres)
                #if not dept.isdigit() or len(dept) != 2:
                    #continue
                
                # Vérifier que le nombre est un entier positif
                try:
                    nombre = int(nombre)
                    if nombre < 0:
                        continue
                except ValueError:
                    continue
                
                # Vérifier que l'année est valide (4 chiffres)
                if not annais.isdigit() or len(annais) != 4:
                    continue
                
                # La ligne est valide, l'écrire dans le fichier de sortie
                writer.writerow(row)
                valid_lines += 1
    
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return
    
    print(f"Traitement terminé.")
    print(f"Lignes traitées: {total_lines}")
    print(f"Lignes valides: {valid_lines}")
    print(f"Lignes invalides: {total_lines - valid_lines}")
    print(f"Fichier de sortie: {output_file}")

if __name__ == "__main__":
    validate_csv()