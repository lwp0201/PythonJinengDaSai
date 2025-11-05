n = int(input("n:"))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print(f"{n}是完备数")
else:
    print(f"{n}不是完备数")
