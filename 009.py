N = 1000
for a in range(1, N):
  for b in range(1, N - a + 1):
    c = N - a - b
    if a * a + b * b == c * c:
      print(a * b * c)
      exit()
