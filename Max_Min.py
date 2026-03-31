 def max_min(x):
...     max=x[0]
...     min=x[0]
...     for i in x:
...         if i>max:
...             max=i
...         if i<min:
...             min=i
...     return max,min
... x=list(int(x) for x in input("enter the number ").split())
... a,b=max_min(x)
... print("min= ",a)
... print("max= ",b)


#output
enter the number 1 22 3 4 5 7 0
min=  22
max=  0
