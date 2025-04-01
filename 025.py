# [ϕ^n - (1 - ϕ)^n] / √5 ≥ 10^999   (binet's theorem) 
# ϕ^n ≥ 10^999 * √5                 ((1 - ϕ)^n term approaches 0)
# n ≥ log(10^999 * √5, ϕ)
# or
# n ≥ [999 + log(√5, 10)] / log(ϕ, 10)

from math import log10

ϕ = (1 + 5 ** 0.5) / 2
print(int((999 + log10(5 ** 0.5)) / log10(ϕ)) + 1)
