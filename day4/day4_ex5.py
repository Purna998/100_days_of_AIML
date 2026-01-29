#Sets
numbers={1,2,3,4}

empty_set=set()

#Adding and Removing items
print(numbers)
numbers.add(5)
print(numbers)

numbers.remove(2) #Remove value 2
print(numbers)

set1={1,2,3}
set2={3,4,5}
print(set1|set2) #Union of two sets
print(set1&set2) #Intersection of two sets
print(set1-set2) #complement set1-set2