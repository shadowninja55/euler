from ast import literal_eval

NS = sorted(literal_eval("[" + open("022.txt").read() + "]"))
A = lambda n: sum(ord(c) - ord("A") + 1 for c in n)
print(sum(i * A(n) for i, n in enumerate(NS, 1)))
