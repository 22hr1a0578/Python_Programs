a=int(input("Enter the number"))
isPrime=True
for i in range(2,a//2):
    if(a%i==0):
        isPrime=False
        break
if(isPrime) & (a>1):
    print("Prime")
else:
    print("Not prime")
