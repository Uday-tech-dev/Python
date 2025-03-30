a=int(input('Enter the Number'))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("The number  isn't a palindrome")
