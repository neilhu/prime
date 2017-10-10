''' Input number and test for prime '''

def prime(x):
	y = 2
	while x % y != 0:
		y = y + 1
	if y == x:
		return "prime"
	elif y < x - 1:
		return "not prime"

px=input("what number should I test for prime? ")
pnum = prime(px)
print px,"is",pnum