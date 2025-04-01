from ast import literal_eval

def T(t):
  n = (-1 + (1 + 8 * t) ** 0.5) / 2
  return n.is_integer()

WS = literal_eval("[" + open("042.txt").read() + "]")
print(sum(T(sum(ord(c) - ord('A') + 1 for c in w)) for w in WS))
