def gen_primes(n):
    primes = [2]
    a = 3
    while len(primes) != n:
        if all(a%i for i in range(2, int(a**0.5) + 2)):
            primes.append(a)
        a += 1
    return primes

primes = gen_primes(10001)
print(primes.pop())