#!/usr/bin/env python2
# filepath: c:\Users\ziyad\OneDrive\Bureau\mini-projet-hadoop\python2\reducer.py
import sys

current_key = None
total = 0

for line in sys.stdin:
    key, count = line.strip().split("\t")
    count = int(count)

    if key == current_key:
        total += count
    else:
        if current_key is not None:
            print "{0}\t{1}".format(current_key, total)
        current_key = key
        total = count

# Ne pas oublier le dernier !
if current_key is not None:
    print "{0}\t{1}".format(current_key, total)