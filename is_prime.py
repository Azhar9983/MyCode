def is_prime(n):
    if(n<2):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
            i+=1
        if(n==i):
            return True
