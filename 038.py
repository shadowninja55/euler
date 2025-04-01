from util import digits, decode

DS = list(range(1, 10))
a, r = 1, None
for a in range(1, 100_000):
  n, ds = 1, []
  while len(ds) < 9:
    ds += digits(a * n)
    n += 1
  if sorted(ds) == DS:
    r = decode(ds)
print(r)
