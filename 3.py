def is_prime(a):
    if a == 2:
        return True

    return all(a%i != 0 for i in ([2] + [i for i in range(3, int(a**0.5) + 2, 2)]))

def largest_prime(b):
    while not is_prime(b):
        for i in range(2,b):
            if is_prime(i) and b%i == 0:
                b = int(b/i)
                break

    return b

n = 600851475143
print(largest_prime(n))