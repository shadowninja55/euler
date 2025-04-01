from util import sieve, digits

U = 10_000
S = sieve(U)
for a in range(U):
  if a == 1487:
    continue
  for d in range(1, (U - a) // 2):
    ns = [a, a + d, a + d + d]
    ds = [sorted(digits(n)) for n in ns]
    if all(S[n] for n in ns) and ds[0] == ds[1] == ds[2]:
      print("".join(map(str, ns)))
      exit()
