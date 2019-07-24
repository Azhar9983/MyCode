def fact(n):
    fact = 1
    for i in range(n,1,-1):
        fact *= i
    return fact
def is_strong(num):
    num1 = num
    result = 0
    while(num>0):
        rem = num%10
        result += fact(rem)
        num //= 10
    if(result == num1):
        return True
    else:
        return False
        
       
        
    
