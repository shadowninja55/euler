from util import primes

def C(d):
  a, l = 10, 0
  while a != 1:
    a = a * 10 % d
    l += 1
  return l + 1

P = primes(1000)[3:]
print(max(P, key=C))
