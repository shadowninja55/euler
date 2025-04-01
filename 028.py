# S(1) = 1
# S(n) = S(n - 2) + 4n^2 - 6(n - 1)

# h = (n - 1) / 2
# S(n) = Σ(k=0, h, 4(2k + 1)^2 - 12k)
# lots of algebra ensues for a closed form

h = (1001 - 1) // 2
print(1  + (16 * h ** 3 + 30 * h ** 2 + 26 * h) // 3)
