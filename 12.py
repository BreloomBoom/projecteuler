from functools import reduce

def tri(n):
    return sum([x for x in range(1,n+1)])

def factors(n):
    return len(set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1) if n % i == 0))))

def high(n):
    curr = 1
    while True:
        if factors(tri(curr)) > n:
            return tri(curr)

        curr += 1

if __name__ == "__main__":
    print(f"{high(500)}")