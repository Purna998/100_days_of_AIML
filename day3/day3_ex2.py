#local scope
def greet():
    message="Hello World"
    print(message)
greet()
# print(message)  # this message has local scope to greet function only

#Global Scope
greeting="Hi"
def say_hello():
    print("Inside function",greeting)
say_hello()
print("Outside function",greeting)