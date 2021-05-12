sX = 3
fX = 20
divisor = 2
for countX in range(3, fX):
    #print(countX)
    # start countX - 1
    while divisor <= (countX - 1):
        #print(divisor, end = '-')
        remainder = countX % divisor
        #print(remainder)
        if remainder == 0:
            #print(countX)
            numPrime = "not prime"
        else:
            #print(countX)
            numPrime = "is prime number"
        divisor = divisor + 1
    print(countX, numPrime)
    divisor = 2
