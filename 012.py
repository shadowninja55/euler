from util import divisors

t, i = 0, 1
while True:
  if len(divisors(t)) > 500:
    print(t)
    break
  t += i
  i += 1
