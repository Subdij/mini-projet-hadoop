#!/bin/bash
# A faire
# rendre le fichier exectubable : chmod +x transfert_vers_vm.sh
# lancez-la avec ./transfert_vers_vm.sh

# === CONFIGURATION ===
CSV_FILE="ParDepartementDepuis2000.csv"
SCRIPT_PIG="/home/maria_dev/script.pig"
HDFS_DIR="/user/maria_dev/test1"
HDFS_HOME="/user/maria_dev"
LOCAL_HOME="/home/maria_dev"



echo "Création du répertoire HDFS : $HDFS_DIR"
hdfs dfs -mkdir -p $HDFS_DIR


echo "Déplacement dans le dossier de travail..."
cd $LOCAL_HOME || exit

echo "Copie du fichier CSV dans HDFS..."
hdfs dfs -mkdir -p $HDFS_HOME/
hdfs dfs -put -f $CSV_FILE $HDFS_HOME/

echo "Exécution du script Pig (et affichage des 10 premières lignes)..."
pig -x mapreduce $SCRIPT_PIG | head -n 10
