from util import sieve, primes

U = 1_000_000
S = sieve(U)
P = primes(U)
m, p = 0, None

for i in range(len(P)):
  s = 0
  for j in range(len(P) - i):
    s += P[i + j]
    if s >= U:
      break
    if S[s] and j - i > m:
      m, p = j - i, s

print(p)
