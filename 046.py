from util import primes, sieve

U = 100_000
P = primes(U)
S = sieve(U)

for n in range(9, U, 2):
  if S[n]: 
    continue
  for p in P:
    d = n - p
    if d < 2:
      print(n)
      exit()
    if ((d / 2) ** 0.5).is_integer():
      break
