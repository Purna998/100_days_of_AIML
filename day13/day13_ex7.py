# Combine multiple plots in a single figure using Matplotlib's subplot
import matplotlib.pyplot as plt
import numpy as np
# First create some toy data:
# Bar Chart 
categories=["Electronic","Clothing","Groceries"]
revenue=[250,400,150]

expenditure = [3,4,2,7,5,4,4,3,3,3,3,8,7,8]
income = [4,3,3,2,6,6,3,3,1,2,9,9,4,5]

fig,ax=plt.subplots(1,2) # 1 row 2 columns
fig.suptitle("Sales details in business")
ax[0].bar(categories,revenue,color="blue")
ax[1].hist([expenditure,income],alpha=0.5, label=["Expenditure","Income"],color=["blue","green"],edgecolor="black")
plt.legend()
ax[0].set_title("Revenue in different categories")
ax[1].set_title("Expenditure vs Income")
ax[1].legend()
plt.show()