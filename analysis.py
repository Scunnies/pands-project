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


"""
# a quick print exercise to see that all my data is correct and accessible
# print (iris)

# This function indicates whether values are missing an array-like object,
# such as this dataframe
print("\n\n\nConfirming that there are no missing or null values in the dataset:\n")
print(data.isna().sum())

# print a concise summary of the iris dataframe information. 
print("\n\n\nThis is a concise summary of the iris dataframe:\n")
print (data.info())

# the dataframe.describe function from PANDAS generates descriptive statistics
# and can be used to output a summary of each variable which I have stored in a
# text file called "VariableSummary"
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

with open("VariableSummary.txt", "w") as f:
    f.write("\nThese are the summary statistics for the Fischer Iris Data Set:\n\n")
    f.write(str(data.describe()))
f.close()
"""
#Histogram of each of the variables in the data set

#dataframe.hist() from Pandas will generate a histogram of each column of variables
#I set bins to auto rather than specify a number
data.hist (alpha = 0.75, color = ['orange'], edgecolor='w', bins = 'auto', figsize=(10,5))

# note plt.title put the title in the middle of the page, across the plots so I found the resolution
# at https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.suptitle.html
plt.suptitle("Histograms of the the Iris Data Set")
plt.savefig("Histograms.png")


#scatterplot of each pair of variables, colour coded by their flower classification
sns.pairplot (data, hue = "class")
plt.suptitle ("Scatterplots of Iris Data Set Variables")
plt.savefig ("Scatterplots.png")
plt.show()