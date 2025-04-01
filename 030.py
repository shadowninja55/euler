from util import digits
from itertools import combinations_with_replacement

P = [d ** 5 for d in range(10)]
S = lambda ds: sum(P[d] for d in ds)
r = 0

for ds in combinations_with_replacement(range(10), 6):
  n = S(ds)
  if n == S(digits(n)):
    r += n

print(r - 1) # exclude 1 = 1^5
