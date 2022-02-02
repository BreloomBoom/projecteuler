def fact(n):
    no = 1
    for i in range(1, n+1):
        no *= i
    return no

print(int(fact(40)/(fact(20)**2)))