N = lambda l: sum(len(w) for w in l)

digits = N(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
teens = N(["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"])
tens = N(["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"])

print(100 * digits + 9 * 100 * len("hundred") + 9 * 99 * len("and") + 10 * sum([digits, teens, 10 * tens, 8 * digits]) + len("onethousand"))
