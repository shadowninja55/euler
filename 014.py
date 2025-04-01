M, N = 0, None
for i in range(1, 1_000_000):
  c, n = 0, i
  while n != 1:
    n = 3 * n + 1 if n % 2 else n // 2
    c += 1
  if c > M:
    M, N = c, i
print(N)
