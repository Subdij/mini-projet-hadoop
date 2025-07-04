#!/usr/bin/env python2
# filepath: c:\Users\ziyad\OneDrive\Bureau\mini-projet-hadoop\python2\mapper.py
import csv
import sys

def mapping():
    try:
        # Utiliser sys.stdin au lieu d'un fichier specifique
        reader = csv.reader(sys.stdin, delimiter=';')
            
        # Ignorer l'en-tete
        header = next(reader, None)
            
        for row in reader:
            sexe, preusuel, annais, dpt, nombre = row
            
            # Calculer la decennie (ex: pour 1985 -> 1980)
            decennie = (int(annais) // 10) * 10
            
            # Creer la cle avec decennie au lieu de l'annee
            key = "{0}_{1}_{2}".format(decennie, sexe, preusuel)
            
            print "{0}\t{1}".format(key, nombre)
            
    except Exception as e:
        print "Une erreur s'est produite: %s" % e
        return        
            
if __name__ == "__main__":
    mapping()