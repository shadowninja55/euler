r = float("-inf")
for x in range(100, 1000):
  for y in range(100, 1000):
    p = x * y
    s = str(p)
    if s == s[::-1]:
      r = max(r, p)
print(r)
