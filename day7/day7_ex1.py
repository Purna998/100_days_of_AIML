# Writing Clean, "Pythonic" Code
# What is Pythonic Code?
# Best Practices 
    #Use descriptive Variable names
    #Write modular code with functions and classes
    #follow PEP 8 style guidelines
    #Avoid redundancy; leverage Python's powerful built-ins

# List Comprehensions - A concise way to create a lists using single line of code
# [expression for item in iterable if condition]

# Create a list of squares
squares=[x**2 for x in range(10)]
print(squares)

# Filter Even numbers
evens=[x for x in range(10) if x%2==0]
print(evens)

odds=[x for x in range(10) if x%2!=0]
print(odds)