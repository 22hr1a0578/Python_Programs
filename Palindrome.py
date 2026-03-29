a=int(input("enter the number"))
b=a
rev=0
while a>0:
    temp=a%10
    rev=rev*10+temp
    a=a//10
if rev == b:
    print("Palindrome")
else:
    print("Not Palindrome")
