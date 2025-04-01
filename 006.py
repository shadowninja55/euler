r = list(range(1, 101))
s = sum(r)
print(s * s - sum(n * n for n in r))
