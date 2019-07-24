def reverse(str):
                    # This is done using RECURSION
    n = len(str)
    while(n>0):
        return reverse(str[1:]) + str[0]
    return str
    
# Here str[1:] says that the string has to start from index 1
# Also + str[0] says to concatenate to str in index 0
