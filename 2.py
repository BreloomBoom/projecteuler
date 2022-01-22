from typing import NewType


a = 0
b = 1
c = 1
while b + c < 4000000:
    if (b + c)%2 == 0:
        a += b+c
    new = b+c
    c = b
    b = new
print(a)