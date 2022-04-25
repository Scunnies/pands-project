# pands project, Programming and Scripting, H.Dip Computing and Data Analytics, 2022
# Author: Eleanor Sammon

# importing libraries which I expect to use
from enum import auto
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

# I have saved the data set to my folder/repository as a CSV file
# it is also available online at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# to load the data set

data = pd.read_csv('iris.csv')



# a quick print exercise to see that all my data is correct and accessible
# print (iris)

print("\n\n\nDisplaying the number of rows and columns are in the dataset:")
print (data.shape)

# This function indicates whether values are missing an array-like object,
# such as this dataframe
print("\n\n\nConfirming that there are no missing or null values in the dataset:\n")
print(data.isna().sum())

# print a concise summary of the iris dataframe information. 
print("\n\n\nThis is a concise summary of the iris dataframe:\n")
data.info()

# the dataframe.describe function from PANDAS generates descriptive statistics
# and can be used to output a summary of each variable which I have stored in a
# text file called "variable_summary"
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

with open("variable_summary.txt", "w") as f:
    f.write("\nThese are the summary statistics for the Fischer Iris Data Set:\n\n")
    f.write(str(data.describe()))
f.close()

## To get specific measurements for each species I can drill down using the groupby function and 
## narrow it down to show only the max and minimum values for each of the classes

print ("\n\nThese are the minimum measurements for each class:\n")
print(data.groupby("class").min())

print ("\n\nThese are the maximum measurements for each class:\n")
print(data.groupby("class").max())


#Histogram of each of the variables in the data set

#dataframe.hist() from Pandas will generate a histogram of each column of variables
#I set bins to auto rather than specify a number
data.hist (alpha = 0.75, color = ['orange'], edgecolor='w', bins = 'auto', figsize=(10,5))

# note plt.title put the title in the middle of the page, across the plots so I found the resolution
# at https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.suptitle.html
plt.suptitle("Histograms of the the Iris Data Set")
plt.savefig("images/Histograms.png") #saved to the images folder for neatness


#scatterplot of each pair of variables, colour coded by their flower classification
sns.pairplot (data, hue = "class")
plt.suptitle ("Scatterplots of Iris Data Set Variables\n\n")
plt.savefig ("images/scatterplots.png")

## a violinplot to give an indication of how the values are distributed
plt.figure(figsize=(10,10))
sns.violinplot(x=data["class"], y=data["sepal_length"])
plt.grid (axis = "y") # I referred to w3schools for how to put in lines on Y axis only
plt.suptitle ("Violinplot of Iris Data Set Species Petal Length\n\n")
plt.savefig ("images/violinplot.png")


# heatmap shown in reds along with the correlation values
# I estimated the figure size (squared seems the norm)
plt.figure(figsize=(10,10))
sns.heatmap(data.corr(), cmap='Reds', annot=True)
plt.suptitle ("Heatmap of Iris Data Set Variables")
plt.savefig ("images/heatmap.png")
