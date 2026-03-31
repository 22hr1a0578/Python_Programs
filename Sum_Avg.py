def cal(x):
...     sum=0
...     avg=0
...     for i in x:
...         sum=sum+i
...         avg=sum/len(x)
...     return sum,avg
... x=list(int(x) for x in input("enter the list").split())
... a,b=cal(x)
... print("Sum= ",a)
... print("avg= ",b)
