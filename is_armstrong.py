def isArmstrong(number):
    n = len(str(number))
    num = number
    res = 0
    while(num > 0):
        rem = num%10
        res += rem**n
        num //= 10
    if(number == res):
        return True
    else:
        return False
