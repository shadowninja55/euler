from itertools import pairwise

def IP(p):
  return ((1 + (1 + 24 * p) ** 0.5) / 6).is_integer()

def P():
  n, d = 1, 4
  while True:
    yield n
    n += d
    d += 3

for d in P():
  for p, pn in pairwise(P()):
    if pn - p > d:
      break
    if IP(p + d) and IP(2 * p + d):
      print(d)
      exit()
