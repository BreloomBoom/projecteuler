largest = 1
for i in range(1000):
    for j in range(1000):
        if str(i*j) == str(i*j)[::-1] and i*j > largest:
            largest = i*j
print(largest)