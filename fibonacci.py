def fibonacci():
    limit = int(input("Enter the limit till which program \nhas to show fibonacci series : \n"))
    #limit = int(input("Enter term limit i.e. \nhow many terms to display : \n"))
    first = 0
    next = 0
    second = 1
    print("`````````````````````````````\n")
    print(first)
    print(second)
    while(limit>next):
        print(next)
        next = first + second
        first = second
        second = next
'''                                                 for i in range(2,limit): 
                                                        next = first + second
              #THIS IS ANOTHER METHOD                   first = second
                                                        second = next
                                                        print(next)

'''
        
fibonacci()

        
        
    
