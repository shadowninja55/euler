from util import divisors

N = 28124
A = [n for n in range(N) if sum(divisors(n)[:-1]) > n]
S = set(A)
r = 0

for n in range(1, N):
  if not any(n - a in S or a + a == n for a in A):
    r += n

print(r)
