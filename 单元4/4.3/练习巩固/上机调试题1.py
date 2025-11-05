for i in range(10):
    for j in range(10):
        n = 67008 + i * 100 + j * 10
        if n % 78 == 0 and n % 67 == 0:
            print(n)
