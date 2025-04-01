n, i, f = 999_999, 1, []
while n > 0:
  n, r = divmod(n, i)
  f.append(r)
  i += 1
  
ds = list(range(10))
for d in f[::-1]:
  print(ds.pop(d), end="")
