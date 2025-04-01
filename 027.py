from util import sieve

PS = sieve(1_000_000)

def P(n):
  assert n < len(PS)
  return n >= 0 and PS[n]

m, ab = float("-inf"), None

for a in range(-999, 1000):
  for b in range(-1000, 1001):
    n = 0
    while P(n * n + a * n + b):
      n += 1
    if n > m:
      m, ab = n, a * b

print(ab)
