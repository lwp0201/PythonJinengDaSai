n = int(input("n:"))
s = 0
for i in range(1, n + 1):
    s += 1 / i / i
pi = 6 * s
pi = pi ** 0.5
print("pi=", pi)
