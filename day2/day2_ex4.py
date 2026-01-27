#Example: break for control flow
for i in range(10):
    if i==5:
        break
    print(i)
print("Outside for loop")

#Example: Continue
for i in range(10):
    if i==5:
        continue
    print(i)
print("Outside for loop")