from util import digits
from math import gcd

N = D = 1

for n in range(10, 100):
  for d in range(n + 1, 100):
    if n % 10 == 0 and d % 10 == 0:
      continue
    ns, ds = digits(n), digits(d)
    for i in range(2):
      if ns[i] == ds[1 - i]:
        nn, dd = ns[1 - i], ds[i]
        if dd != 0 and n / d == nn / dd:
          N *= n
          D *= d 
          break

print(D // gcd(N, D))
