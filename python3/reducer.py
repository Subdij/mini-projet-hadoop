#!/usr/bin/env python3
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
            print(f"{current_key}\t{total}")
        current_key = key
        total = count

# Ne pas oublier le dernier !
if current_key is not None:
    print(f"{current_key}\t{total}")