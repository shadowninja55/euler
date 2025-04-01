x, y, r = 1, 2, 0
while x < 4_000_000:
  if x % 2 == 0:
    r += x
  x, y = y, x + y
print(r)
