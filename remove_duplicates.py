#!/usr/bin/env python3

with open("ParamLabels.csv") as f:
    csv = [line.rstrip('\n').split(',', 1) for line in f.readlines() if not line.isspace()]

hashes = set()
csvout = []
for i in csv:
    hash = int(i[0], 16)
    hashString = f"{hash:#0{12}x}"
    if not hash in hashes:
        hashes.add(hash)
        csvout.append((f"{hashString}", i[1]))

csvout.sort(key=lambda i: i[1])

with open("ParamLabels.csv", 'w') as f:
    f.write('\n'.join([','.join(line) for line in csvout]))
