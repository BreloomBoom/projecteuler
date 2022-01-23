primes = [2]
x = 3
while x < 2000000:
    if all(x%i for i in range(2, int(x**0.5+2))):
        primes.append(x)
    x += 1
print(sum(primes))