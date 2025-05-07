#!/usr/bin/env python2
# filepath: c:\Users\ziyad\OneDrive\Bureau\mini-projet-hadoop\python2\validation.py
import csv
import os
import codecs

def validate_csv():
    input_file = 'nat2022_v2.csv'
    output_file = 'nat2022_valid.csv'
    
    # Verifier si le fichier d'entree existe
    if not os.path.exists(input_file):
        print "Erreur: Le fichier %s n'existe pas." % input_file
        return
    
    total_lines = 0
    valid_lines = 0
    
    try:
        with codecs.open(input_file, 'r', encoding='utf-8') as infile, \
             codecs.open(output_file, 'w', encoding='utf-8') as outfile:
            
            # Creer le lecteur et l'ecrivain CSV
            reader = csv.reader(infile, delimiter=';')
            writer = csv.writer(outfile, delimiter=';')
            
            # Ignorer l'en-tete
            header = next(reader, None)
            
            # Ecrire l'en-tete dans le fichier de sortie (optionnel)
            if header:
                writer.writerow(header)
            
            # Traiter chaque ligne
            for row in reader:
                total_lines += 1
                
                # Verifier que la ligne a exactement 5 champs
                if len(row) != 5:
                    continue
                
                # Verifier que les champs requis ne sont pas vides
                sexe, preusuel, annais, dept, nombre = row
                if not annais or not sexe or not nombre or not dept:
                    continue
                
                # Verifier que le prenom est valide (different de "_PRENOMS_RARES")
                if preusuel == "_PRENOMS_RARES":
                    continue
                
                # Verifer que le sexe est valide (1 ou 2)
                if sexe not in ['1', '2']:
                    continue
                
                # Verifier que le nombre est un entier positif
                try:
                    nombre = int(nombre)
                    if nombre < 0:
                        continue
                except ValueError:
                    continue
                
                # Verifier que l'annee est valide (4 chiffres)
                if not annais.isdigit() or len(annais) != 4:
                    continue
                
                # La ligne est valide, l'ecrire dans le fichier de sortie
                writer.writerow(row)
                valid_lines += 1
    
    except Exception as e:
        print "Une erreur s'est produite: %s" % e
        return
    
    print "Traitement termine."
    print "Lignes traitees: %d" % total_lines
    print "Lignes valides: %d" % valid_lines
    print "Lignes invalides: %d" % (total_lines - valid_lines)
    print "Fichier de sortie: %s" % output_file

if __name__ == "__main__":
    validate_csv()