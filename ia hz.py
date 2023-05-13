from random import *
e = 1
w = randint(1,9)
while e > 0:
    r = randint(1, 2)
    q = int(input())
    if r == 1:
        e = e - (q*w)
    if r == 2:
        e = e + (q*w)
    print(e)