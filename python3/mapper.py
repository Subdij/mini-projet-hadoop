#!/usr/bin/env python3
import csv
import os

def mapping():
    input_file = 'nat2022_valid.csv'
    
    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_file):
        print(f"Erreur: Le fichier {input_file} n'existe pas.")
        return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
             
            # Créer le lecteur et l'écrivain CSV
            reader = csv.reader(infile, delimiter=';')
            
            # Ignorer l'en-tête
            header = next(reader, None)
            
            for row in reader:
                sexe, preusuel, annais, dpt, nombre = row
                key = f"{annais}_{sexe}_{preusuel}"
                print(f"{key}\t{nombre}")
            
            
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return        
            


if __name__ == "__main__":
    mapping()