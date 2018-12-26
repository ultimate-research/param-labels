with open("ParamLabels.csv") as f:
    csv = [line.rstrip('\n').split(',') for line in f.readlines() if not line.isspace()]

hashes = []
csvout = []
for i in csv:
    if not i[0] in hashes:
        hashes.append(i[0])
        csvout.append(i)

csvout.sort(key=lambda i: i[1])

with open("ParamLabels.csv", 'w') as f:
    f.write('\n'.join([','.join(line) for line in csvout]))