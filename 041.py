from util import primes, digits

for p in reversed(primes(7654321 + 1)):
  ds = digits(p)
  if sorted(ds) == sorted(range(1, len(ds) + 1)):
    print(p)
    exit()
