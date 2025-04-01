from util import divisors

DS, r = [0] * 10000, 0

for n in range(10000):
  DS[n] = dn = sum(divisors(n)[:-1])
  if dn < n and DS[dn] == n:
    r += n + dn

print(r)
