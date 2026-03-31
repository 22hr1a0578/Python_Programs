 def data(name,*marks): #assigning variable length argument by *
...     print("name = %s" %name)
...     print("marks = ",marks)
...     print(type(marks))
... data("Latha",10,1,23,2,11,6,55)
...
#output
name = Latha
marks =  (10, 1, 23, 2, 11, 6, 55)
<class 'tuple'>
