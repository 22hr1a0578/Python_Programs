#1
#assigning function to a variable
def assign(a):
...     return "hii "+a
... x=assign("guys----!")
... print(x)
...
#output
hii guys----!


#2
#defining a function inside a function
 def display(s):
...     def message():
...         return "how are you"
...     return s+message()
... print(display("hello......"))
...
#output
hello......how are you


#3
#passing function as a parameter
 def hello(d):
...     return "hi " +d
... def message():
...     return "Hello"
... hello(message())
...
#output
'hi Hello'


#4
#function return another function
ction a.<locals>.b at 0x000002B47E8040F0>
>>> def a():
...     def b():
...         return "hi"
...     return b()
...
... print(a())
...
#Output
hi
