from util import decode, digits, sieve, primes

S = sieve(1_000_000)
P = primes(1_000_000)

def R(a):
  n = len(a)
  return [[a[(i + j) % n] for j in range(n)] for i in range(n)]

print(sum(all(S[decode(r)] for r in R(digits(p))) for p in P))
