#!/usr/bin/python
""" Input number and test for prime """
sx = 0
ex = 0

def prime(x):
    # test prime
    y = 2
    while x % y != 0:
        y = y + 1
    if y == x:
        return "prime"
    elif y < x - 1:
        return "not prime"

while sx < 2 or ex < 2:
    print "This will list all primes between 2 numbers (greater than 1)"
    sx, ex = input("what number should start and end at? ")

for i in range(sx, ex + 1):
    pnum = prime(i)
#    print pnum
#    print i
    if pnum == "prime":
        print i,"is",pnum
