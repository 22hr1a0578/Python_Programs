 def kwlen(name,**values): #keyword variable length argument
...     print("name =%s"%name)
...     print(values)
... kwlen("latha",name1="Latha",age=22,salary=22000)
...

#Output
name =latha
{'name1': 'Latha', 'age': 22, 'salary': 22000}

#fetch items from kwarg
 def kwarg(**b):
...     print(type(b))
...     for c,d in b.items():
...         print("Keys ={}".format(c))
...         print("values={}".format(d))
... kwarg(name="Latha",age=22,salary=22000)
...

#output
<class 'dict'>
Keys =name
values=Latha
Keys =age
values=22
Keys =salary
values=22000


#fetching only keys
def kwarg(**b):
...     for c in b.keys():
...         print("keys={}".format(c))
... kwarg(name="Latha",age=22,salary=22000)
...

#output
keys=name
keys=age
keys=salary

#fetching values
def kwarg(**b):
...     for c in b.values():
...         print("values={}".format(c))
... kwarg(name="Latha",age=22,salary=22000)
...

#output
values=Latha
values=22
values=22000
