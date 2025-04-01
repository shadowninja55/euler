def W(t, cs):
  if t <= 0:
    return t == 0
  return sum(W(t - c, cs[i:]) for i, c in enumerate(cs))

print(W(200, [1, 2, 5, 10, 20, 50, 100, 200]))
