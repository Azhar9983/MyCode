
def find_lcm(n1,n2):
    if(n1>n2):
        large = n1
    else:
        large = n2
    while(True):
        if(large%n1==0 and large%n2==0):
            return large
            break
        large += 1
        
def n_lcm():
    list = [int(list) for list in input("Enter multiple values: ").split()]
    num1 = list[0] 
    num2 = list[1] 
    lcm = find_lcm(num1, num2) 
  
    for i in range(2, len(list)): 
        lcm = find_lcm(lcm, list[i]) 
    print("LCM of all ",list," is ",lcm)
            
