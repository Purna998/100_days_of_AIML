# Calculate the factorial of a number using a while loop
num=int(input("Enter a number:"))
fact=1
while num!=0:
    fact=fact*num
    num-=1
print(f"Factorial of a number:{fact}")