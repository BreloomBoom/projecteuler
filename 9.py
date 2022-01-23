def triad():
    for i in range(1,1000):
        for j in range(1,1000):
            n = i**2 + j**2
            if int(n**0.5) == n**0.5 and i + j + n**0.5 == 1000:
                return i*j*int(n**0.5)

print(triad())