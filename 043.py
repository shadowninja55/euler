from itertools import permutations
from util import decode

P = [2, 3, 5, 7, 11, 13, 17]
r = 0
for ds in permutations(range(10)):
  for i in range(1, 8):
    if decode(ds[i:i+3]) % P[i - 1] != 0:
      break
  else:
    r += decode(ds)
print(r)
