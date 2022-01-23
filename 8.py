def process(no):
    return open(no, "r").read().replace("\n", "")

def prod(nos):
    final = 1
    for i in nos:
        final *= int(i)
    return final

no = process("/Users/breloom/Code/projecteuler/8.txt")
max = 0
for i in range(len(no)-12):
    if prod([no[i + a] for a in range(13)]) > max:
        max = prod([no[i + a] for a in range(13)])

print(max)