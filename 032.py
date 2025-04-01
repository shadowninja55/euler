from functools import reduce
from itertools import permutations
from util import decode

DS = permutations(range(1, 10))
r = set()

for ds in DS:
  for i in range(1, 8):
    for j in range(i + 1, 9):
      a = decode(ds[:i])
      b = decode(ds[i:j])
      c = decode(ds[j:])
      if a * b == c:
        r.add(c)

print(sum(r))
