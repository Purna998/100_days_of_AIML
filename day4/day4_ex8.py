# Write a program to reverse a list and remove duplicates using a set

list_var=[1,2,3,4,5]
# list_var.sort(reverse=True)
# print(list_var)


list_var = [1, 2, 3, 4, 5,3,1]

for i in range(len(list_var)):
    for j in range(i + 1, len(list_var)):
        if list_var[i] < list_var[j]:
            a=list_var[i]
            list_var[i]=list_var[j]
            list_var[j]=a
            
print(list_var)  

set_var=set(list_var)
print(set_var)



