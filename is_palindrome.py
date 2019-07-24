def isPalindrome(str):
        if(str == "".join(reversed(str))):
                print("String is Palindrome")
        else:
                print("String isn't Palindrome")
new = str(input("Enter SomeThing : "))
isPalindrome(new)
