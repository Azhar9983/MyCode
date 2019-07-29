import sys
#FUNCTION FOR FINDING FACTORIAL OF NUMBER N
def fact(n):
    fact = 1
    for i in range(n,1,-1):
        fact *= i
    return fact
#DRIVER CODE TO RUN FROM COMMAND LINE
print(fact(int(sys.argv[1])))
