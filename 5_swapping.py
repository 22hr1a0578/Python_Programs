#Swapping two numbers without using third variable
a=10
b=1
a=a+b
b=a-b
a=a-b
print(a,b)


#Swapping using divison And Multiplication
a=10
b=1
a=a*b
b=a//b
a=a//b
print(a,b)


#Swapping using xor gate
a=10
b=1
a=a^b
b=a^b
a=a^b
print(a,b)

#python special method for Swapping 
a=10
b=1
a,b=b,a
print(a,b)

#using temp
a=10
b=1
temp=a
a=b
b=temp
print(a,b)
