#!/usr/bin/env python3

with open("Labels.txt") as f:
    csv = [line.rstrip('\n') for line in f.readlines() if not line.isspace()]

csvout = sorted(set(csv))

with open("Labels.txt", 'w') as f:
    f.write('\n'.join(csvout))
