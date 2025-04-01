r = 0
for n in range(1_000_000):
  s = str(n)
  b = str(bin(n))[2:]
  if s == s[::-1] and b == b[::-1]:
    r += n
print(r)
