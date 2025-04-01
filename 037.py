from util import digits, decode, sieve

S = sieve(1_000_000)

def Tl(ds):
  if not ds:
    return True
  return S[decode(ds)] and Tl(ds[1:])

def Tr(n):
  if n == 0:
    return True
  return S[n] and Tr(n // 10)

r, n = [], 8
while len(r) < 11:
  if Tl(digits(n)) and Tr(n):
    r.append(n)
  n += 1
print(sum(r))
