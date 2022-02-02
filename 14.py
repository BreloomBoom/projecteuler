def collatz(n):
    no = 1
    while n != 1:
        if n % 2:
            n = 3*n + 1
        else:
            n /= 2
        no += 1
    return no

maxi = 0
no = 0
for i in range(1, 1000001):
    n = collatz(i)
    if maxi < n:
        maxi = n
        no = i

print(no)