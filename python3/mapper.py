#!/usr/bin/env python3
import csv
import os

def mapping():
    try:
        # Utiliser sys.stdin au lieu d'un fichier spécifique
        reader = csv.reader(sys.stdin, delimiter=';')
            
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