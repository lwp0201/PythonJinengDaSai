# 质数的和与积
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


S = int(input())
max_product = 0
for i in range(2, S):
    if is_prime(i) and is_prime(S-i):
        max_product = max(max_product, i*(S-i))
print(max_product)