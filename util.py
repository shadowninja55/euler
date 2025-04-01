import numpy as np
from functools import reduce

def sieve(n):
  P = np.ones(n, dtype=bool)
  P[:2] = False
  for p in range(2, n):
    if P[p]:
      P[p*p::p] = False
  return P

def primes(n):
  return np.flatnonzero(sieve(n))

def decompose(n):
  p, r = 2, []
  while n > 1:
    if n % p == 0:
      r.append(p)
      n //= p
    else:
      p += 1
  return r

def digits(n):
  r = []
  while n > 0:
    r.append(n % 10)
    n //= 10
  return r[::-1]

def divisors(n):
  l, r = [], []
  for d in range(1, int(n ** 0.5 + 1)):
    q, m = divmod(n, d)
    if not m:
      l.append(d)
      if q != d:
        r.append(q)
  return l + r[::-1]

def decode(ds):
  return reduce(lambda a, d: a * 10 + d, ds, 0)
