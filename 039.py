from numpy import argmax

S = [0] * 1001

for p in range(3, 1000):
  for a in range(1, p - 1):
    for b in range(a, p - a):
      c2 = (p - a - b) ** 2
      h = a * a + b * b
      if h > c2:
        break
      if h == c2:
        S[p] += 1

print(argmax(S))
