# Create a program to find the largest number in a list using a for loop
list_var=[13,8,3,1,52,24]
list_size=len(list_var)
largest=list_var[0]
for i in range(1,list_size):
    # print(list_var[i])
    if (list_var[i]>largest):
        largest=list_var[i]
print(f"Largest Number in list:{largest}")
    