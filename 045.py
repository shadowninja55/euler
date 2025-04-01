def TS():
  n, d = 1, 2
  while True:
    yield n
    n += d
    d += 1

def P(p):
  return ((1 + (1 + 24 * p) ** 0.5) / 6).is_integer()

def H(h):
  return ((1 + (1 + 8 * h) ** 0.5) / 6).is_integer()

for t in TS():
  if t > 40755 and P(t) and H(t):
    print(t)
    break
