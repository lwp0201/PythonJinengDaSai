#素数回文数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

#a,b = map(int,input().split())
for i in range(10, 1000):
    if is_prime(i) and str(i) == str(i)[::-1]:
        print(i)