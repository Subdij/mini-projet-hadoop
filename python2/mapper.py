#!/usr/bin/env python2
# filepath: c:\Users\ziyad\OneDrive\Bureau\mini-projet-hadoop\python2\mapper.py
import csv
import os
import sys

def mapping():
    input_file = 'nat2022_valid.csv'
    
    # Verifier si le fichier d'entree existe
    if not os.path.exists(input_file):
        print "Erreur: Le fichier %s n'existe pas." % input_file
        return
    
    try:
        with open(input_file, 'r') as infile:
             
            # Creer le lecteur CSV
            reader = csv.reader(infile, delimiter=';')
            
            # Ignorer l'en-tete
            header = next(reader, None)
            
            for row in reader:
                sexe, preusuel, annais, dpt, nombre = row
                key = "{0}_{1}_{2}".format(annais, sexe, preusuel)
                print "{0}\t{1}".format(key, nombre)
            
    except Exception as e:
        print "Une erreur s'est produite: %s" % e
        return        
            
if __name__ == "__main__":
    mapping()