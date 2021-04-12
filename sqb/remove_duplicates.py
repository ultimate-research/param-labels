#!/usr/bin/env python3

with open("Labels.txt") as f:
    csv = [line.rstrip('\n').split(',', 1) for line in f.readlines() if not line.isspace()]
motionList = []
for i in csv:
    if not i in motionList:
        motionList.append(i)

motionList.sort(key=lambda i: i)

with open("Labels.txt", 'w') as f:
    f.write('\n'.join([','.join(line) for line in motionList]))
