# pands project, Programming and Scripting, H.Dip Computing and Data Analytics, 2022
# Author: Eleanor Sammon

# importing libraries which I expect to use
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
import re

# I have saved the data set to my folder/repository as a CSV file
# it is also available online at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# to load the data set
data = pd.read_csv('iris.csv')

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
