# Measure of Dispersion
data=[10,20,30,40,50]
mean=sum(data)/len(data)

variance=sum((x - mean)**2 for x in data) / len(data)
print("Variance: ",variance)


std_dev=variance**0.5
print("Standard Deviation: ",std_dev)