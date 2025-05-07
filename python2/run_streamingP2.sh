#!/bin/bash

# 1. Copier access.log dans HDFS
hdfs dfs -mkdir -p /user/maria_dev/prenoms/logs
hdfs dfs -put -f nat2022_valid.csv /user/maria_dev/prenoms/logs/

# 2. Supprimer l’ancien dossier de sortie
hdfs dfs -rm -r /user/maria_dev/prenoms/logs/output

# 3. Rendre les scripts exécutables localement
chmod +x mapper.py
chmod +x reducer.py

# 4.  Lancer Hadoop Streaming
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-input /user/maria_dev/prenoms/logs/nat2022_valid.csv \
-output /user/maria_dev/prenoms/logs/output \
-mapper mapper.py \
-reducer reducer.py \
-file mapper.py \
-file reducer.py