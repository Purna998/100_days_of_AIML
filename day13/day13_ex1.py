# Matplotlib - Foundation data visualization python library
# Add titles, axis,labels and legends
# Adjust colors and styles
import matplotlib.pyplot as plt
# Basic plot 
x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y)
plt.show()

# Line Plot 
plt.plot([1,2,3,4],[40,10,50,20],label="Trend",color="orange",linestyle="--",marker="o") # marker="x"
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# Bar Chart - Categorical Data Comparison
categories=["A","B","C"]
values=[10,15,7]
plt.bar(categories,values,color="blue")
plt.title("Bar Chart")
plt.show()

# Histogram - continuous numerical data frequency distribution
data=[1,2,3,3,3,3,4,5,3,8,8,6,6,3]
plt.hist(data,bins=4,color="green",edgecolor="black")
plt.title("Histogram")
plt.show()
 
# Scatter Plot
x=[1,2,3,4,5]
y=[10,23,12,65,43]
plt.scatter(x,y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.xlabel("Y-axis")
plt.legend(["Dataset1"])
plt.show()