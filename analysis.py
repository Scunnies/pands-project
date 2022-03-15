# pands project, Programming and Scripting, H.Dip Computing and Data Analytics, 2022
# Author: Eleanor Sammon

# importing libraries which I expect to use
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

# I have saved the data set to my folder/repository as a CSV file
# it is also available online at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# to load the data set
data = pd.read_csv('iris.csv')

# a quick print exercise to see that all my data is correct and accessible
print (data)