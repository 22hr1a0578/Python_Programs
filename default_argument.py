 def grocery(items,price=10):
...     print("items = %s" %items)
...     print("Price = %2f" %price)
... grocery(items="sugar")

#output
items = sugar
Price = 10.000000

#adding another value to price
>>> def grocery(items,price=10):
...     print("items = %s" %items)
...     print("Price = %2f" %price)
... grocery(items="sugar")
... grocery(items="ssss",price=16)
...

#output
items = sugar
Price = 10.000000
items = ssss
Price = 16.000000
