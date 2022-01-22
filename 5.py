def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

stuff = {}
for i in range(1,21):
    factors = prime_factors(i)
    for j in factors:
        if j not in stuff:
            stuff.update({j: factors.count(j)})
        else:
            if stuff[j] < factors.count(j):
                stuff[j] = factors.count(j)

final = 1
for k in stuff:
    final *= k**stuff[k]

print(final)