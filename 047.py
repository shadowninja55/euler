from util import decompose
from collections import deque

n, d = 2, deque([False] * 4, maxlen=4)
while True:
  d.append(len(set(decompose(n))) == 4)
  if all(d):
    print(n - 3)
    break
  n += 1
