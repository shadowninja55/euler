F = [1] * 10
for i in range(1, 10):
  F[i] = F[i - 1] * i
S = lambda n: sum(F[int(d)] for d in str(n))
print(sum(n for n in range(3, 8 * F[9]) if n == S(n)))
