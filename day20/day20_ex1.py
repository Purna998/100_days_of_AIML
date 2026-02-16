from statistics import mode
# Measures of Central Tendency
data=[10,20,30,40,50]
mean=sum(data)/len(data)
print("Mean: ",mean)

sorted_data=sorted(data)
median=sorted_data[len(data)//2] if len(data) !=0 else \
    (sorted_data[len(data)//2-1]+sorted_data[len(data)//2])/2
print("Median: ",median)

print("Mode: ",mode(data))

