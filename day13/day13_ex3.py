# Create dataset and basic plots with matplotlib

import matplotlib.pyplot as plt

# Line plot
years=[2010,2011,2012,2013]
sales=[100,120,140,160]
plt.plot(years,sales,label="Sales Trend",color="blue",marker="o",linestyle="--")
plt.title("Sales over years")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar Chart 
categories=["Electronic","Clothing","Groceries"]
revenue=[250,400,150]
plt.bar(categories,revenue,color="blue")
plt.title("Bar Chart")
plt.show()

# Scatter Plot
hours_studied=[1,2,3,4,5]
exam_scores=[50,55,65,70,85]
plt.scatter(hours_studied,exam_scores,color="red")
plt.title("Study hours vs exam_scores")
plt.xlabel("Hours Study")
plt.ylabel("Exam Score")
plt.show()