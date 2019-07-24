
def gcd(a,b):
    if(a<b):
        small = a
    else:
        small = b
    while(small>0):
        if(a%small==0 and b%small==0):
            return small
            break
        small -= 1

def n_gcd():
    list = [int(list) for list in input("Enter Multiple numbers : ").split()]
    num1 = list[0]
    num2 = list[1]
    gcd1 = gcd(num1,num2)

    for i in range(2,len(list)):
        gcd1 = gcd(gcd1,list[i])
    print("GCD of the list ",list, "is ",gcd1)

        #write n_gcd() in shell to start program
