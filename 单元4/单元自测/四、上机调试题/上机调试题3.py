s = 'ABCD'
n = len(s)
for i in range(n):
    print(" " * (n - i), s[i] * (2 * i + 1))
