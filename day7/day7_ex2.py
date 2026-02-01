# Lambda Functions
# Anonymous, single-expression functions defined using the lambda keyword

# using def
def add(x,y):
    return x+y
print(f"{add(1,2)}")

# using lambda
add=lambda x,y:x+y
print(add(1,2))

# map()-Applies a function to each item in an iterable
numbers=[1,2,3,4]
squares=map(lambda x:x**2,numbers)
print(list(squares))

# filter()-Filters items based on condition
evenList=filter(lambda x:x%2==0,numbers) # check whether items in list is even or not
print(list(evenList))

# reduce() - Reduces an iterable to a single value from functools
from functools import reduce
numbers=[1,2,3,4] #1*2=2, 2*3=6, 6*4=24(result=previous result * next number)
product=reduce(lambda x,y:x*y,numbers)
print(product)