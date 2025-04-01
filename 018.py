from functools import reduce
from operator import add

T = [[int(i) for i in l.split()] for l in open("018.txt")][::-1]
p = reduce(lambda x, y: list(map(add, map(max, x, x[1:]), y)), T)
print(p[0])
