def fact(n):
    fact = 1
    for i in range(n,1,-1):
        fact *= i
    return fact
