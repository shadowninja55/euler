from math import prod

ds = [int(d) for d in "".join(l.strip() for l in open("008.txt"))]
print(max(prod(ds[i:i+13]) for i in range(0, len(ds) - 12)))
