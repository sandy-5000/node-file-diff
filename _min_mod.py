
def is_prime(n):
    if i == 2:
        return True
    if i < 2 or i % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


print('Flag:', is_prime(17))
