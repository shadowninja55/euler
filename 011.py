from math import prod

G = [[int(s) for s in l.strip().split()] for l in open("011.txt")]
M = 0
DS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
for i in range(20):
  for j in range(20):
    for dj, di in DS:
      p = prod(G[i + di * k][j + dj * k] for k in range(4) if 0 <= i + di * k < 20 and 0 <= j + dj * k < 20)
      M = max(M, p)
print(M)
