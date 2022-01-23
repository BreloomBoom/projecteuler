n = 100
print(int((n/2*(n+1))**2-sum([(x+1)**2 for x in range(n)])))