from math import prod
from util import digits

n, f = 1, []
while len(f) < 1_000_000:
  f += digits(n)
  n += 1
print(prod(f[10 ** i - 1] for i in range(7)))
