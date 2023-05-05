def primeNumber(x):
    count = 0
    for i in range(1, x+1):
        if(x%i == 0):
            count += 1
    if(count == 2):
        return 1 # Prime number
    else:
        return 0 # not Prime number
    
x = int(input("number: "))
    
if(primeNumber(x) == 1):
    print("{0} is prime number".format(x))
else:
    print("{0} isn't prime number".format(x))
