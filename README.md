# pands-project
## Project to analyse the iris data set

# Table of Contents
<a name="-table-of-contents"></a>

1. [Introduction](#1.-introduction) 
2. [Technical Specifications](#2.-technical-specifications)
3. [The Iris Data Set](#3.-the-iris-dataset) 
4. [Investigating the Iris Data Set](#4.-investigating-the-data-set)
5. [Summary & Conclusions](#5.-summary-&-conclusions)
6. [References](#6.-references)
7. [Acknowledgements](#7.-acknowledgements)


## Introduction
<a name="1.-introduction"></a>
This repository contains my pands project on the Fischer Iris Data Set, submitted for assessment under the Programming and Scripting module which in turn forms part of the Higher Diploma in Computing and Data Analytics at GMIT.

In this project I will outline the programs and tools used to build and execute this project before covering the history and provenance of the Fischer iris data set and why it is so widely used in machine learning. 

I will be using VS Code as my source code editor and this accompanying README file outlines the thinking behind coding which I use to introduce, manipulate and present the data therein, discussion of the code used to examine and manipulate the data set, generate informative plots and visualisations from that data and finally summarise my findings and conclusions.

The aim and purpose of this project is to improve upon my Python coding and scripting, learn more about the dynamics of machine learning and the functions and uses of data visualisations. 

 
## Technical Specifications
<a name="2.-technical-specifications"></a>
### How to Download this project

1. Go to the URL for the repository on GitHub at [https://github.com/Scunnies/pands-project.git](https://github.com/Scunnies/pands-project.git))
2. Click the green `Code` button
3. You now have the option to either clone the repository, open with [Github Desktop](https://desktop.github.com/) or download the zip file
 
The script is written in Python and Python 3 is required to run it.  It can be downloaded from [https://www.python.org/downloads/](https://www.python.org/downloads/).  Anaconda and a Command Line program may also be required and these can be downloaded from [https://www.anaconda.com/](https://www.anaconda.com/) and [https://cmder.net/](https://cmder.net/) respectively.

To run the script enter `python analysis.py` on the command line.  Some of the output from the code, such as tables and plots are saved in the images folder and also included as graphics in this README file.

<a name="3.-the-iris-data-set"></a>
## The Iris Data Set – History and Relationship with Machine Learning

### History
There are between 200 and 300 species within the [iris](https://sites.berry.edu/cborer/inventory/iris/) genus so identifying them to this particular family can be challenging.  Most irises do have some shared characteristics however, first among them is the presence of six 'petals'. The inner three petals are referred to as “standards” while the outer three sepals, often mistaken for petals, are called “falls”. Sepals serve as protection for the flower in bud and as support for the petals when in bloom.

The [Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) represents four measurements of floral morphology on 150 plants - 50 individuals for each of three genus (*Iris versicolor*, *Iris setosa*, and *Iris virginica*).  The numeric parameters which the dataset contains are sepal width, sepal length, petal width and petal length.  Classification accuracy is the ratio of number of correct predictions to the total number of input samples, it works best if there are equal number of samples belonging to each class which, in this case, there are.

![Iris Flowers](https://github.com/Scunnies/pands-project/blob/main/images/irisflowers.png)

It was, in fact, [Edgar Shannon Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) (1897 - 1969) who collected the data to quantify the structural variation of Iris flowers of three related species, providing the raw data which formed the basis of the famous iris data set.  His research was focused on developing techniques to quantify geographic variation in *Iris versicolor*. It was, in fact, Anderson who determined the existence of a second species, *Iris virginica* and it was during the 1930’s, as part of this research, that Anderson gathered and documented the dataset which forms the basis of this and no doubt thousands of other machine learning assignments.  In 1929 Anderson received a fellowship to undertake studies at the John Innes Horticultural Institute in Britain, where he worked with cytogeneticist C. D. Darlington, geneticist J. B. S. Haldane and most notably for the purposes of this assignment, statistician R. A. Fisher.  If I were to correlate the Iris data set to Band Aid then Anderson was Midge Ure to Fisher's Geldof, in as much as he gets credited only occasionally!

The Geldof of their relationship was [Sir Ronald Aylmer Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) (1890 – 1962), a British mathematician, statistician, geneticist and academic. For his work in statistics, he has been variously described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics" and was touted as a natural successor to Darwin in terms of his scientific and evolutionary theorising.  Notwithstanding his genius, Fisher had some questionable links to [eugenics](https://en.wikipedia.org/wiki/Eugenics), he was a founding Chairman of the University of Cambridge Eugenics Society in 1911.  Eugenics is a set of beliefs and practices that aim to improve the genetic quality of a human population, historically by excluding people and groups judged to be inferior or promoting those judged to be superior.  Fischer went on to distance himself from the society in 1941 but then, subsequent to World War II, wrote a character reference for a Nazi eugenicist who had inauspicious links to Josef Mengele.   His paper on the Iris data set, which was published in 1936, has been accused of being a tool to advance the science of eugenics, proposing a methodological framework to delineate 'desirable' traits, ostensibly to promote eugenics programs. This is one reason why other data sets are often ushered forth as more morally palatable substitutes.  Alternatives, as suggested by one Data Scientist, [Megan Todal](https://www.meganstodel.com/posts/no-to-iris/), include data on cars (`mpg` from `ggplot2`), hawks (found in the `Stat2Data` package) and mushrooms (data set available on the Machine Learning Repository of the UC Irvine website).   

### Relationship with Machine Learning
Each row in the Iris dataset describes one flower for which there are four seperate measurements - the length and width of the sepals, the length and width of the petals.  The 5th column is the species of iris: *setosa, versicolor*, or *virginica*. 

Despite its shaky provenance the Fisher data set is described as the 'Hello World' for machine learning, useful for practicing basic machine learning algorithms.  It endures because the data is open source, the accuracy and origin are both known, it is 'real' data and with three types of flower, it allows for more than just binary classification.  Additionally, with an even 50 in each classification it is balanced and has no null or missing values.  All measurements are on the same scale (cm) so no normalisation is called for and the file size isn’t unwieldy or excessively complicated.  


<a name="4.-investigating-the-data-set"></a>
## My Investigation of the Data Set Using Python
My first step was to import the libaries that I felt would be most useful in manipulating the data.  The are as follows:
`numpy` - short for Numerical Python and used to perform a wide variety of mathematical operations on arrays
`pandas` - for data manipulation and analysis with data structures and operations for manipulating numerical tables and time series
`matplotlib.pyplot` - a plotting library for creating static, animated, and interactive visualizations in Python
`seaborn` -  based on matplotlib, this data visualization library provides a high-level interface for drawing attractive and informative statistical graphics

Next I imported the data set from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) as iris.csv and read it in and did a quick print check to ensure it was working as intended

`data = pd.read_csv('iris.csv')`
`print (iris)`

### Summary Information
I use `shape` to give me some basic information on my array, namely the number of rows and columns, a simple and useful tool to tell me what I'm dealing with. 

This data set being quite small, very famous and scrutinised to death I already know that the data is ship shape for analysis and doesn't require any tidy-up but it seems also to be good practice when dealing with data to check for null values as a program encountering a null value may return an error.  Missing values are usually represented in the form of Nan, null or None.

To establish null values I used the code `data.isna().sum()` which gives the sum of missing values. 

![Null Values](https://github.com/Scunnies/pands-project/blob/main/images/null_values.png)

Having been down a rabbit hole on this subject, I understand there are many ways to deal with [missing/null values](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/) but it depends on the type of data set in question.  For argument's sake, had I encountered null values in this particular data set I likely would have used the median value to replace them and we will see how that is calculated further on. 

The [Pandas Dataframe `info` method](https://www.w3schools.com/python/pandas/ref_df_info.asp#:~:text=The%20info()%20method%20prints,method%20actually%20prints%20the%20info.) prints information about the DataFrame without the need to actually call the `print()` method. This useful feature gives us the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values). A quick and easy way to get a concise summary of a dataframe. 

![Dataframe](https://github.com/Scunnies/pands-project/blob/main/images/summary.png)

Descriptive or summary statistics can be elicited using the [Pandas dataframe `describe()`](https://www.w3schools.com/python/pandas/ref_df_describe.asp) method, returning information under the following standard headings: 

count - The number of not-empty values
mean - The average (mean) value
std - The standard deviation
min - the minimum value
25% - The 25% percentile
50% - The 50% percentile
75% - The 75% percentile
max - the maximum value

This summary of each variable is output to a text file called "variable_summary.txt". As mentioned previously, if I were to encounter null values in the data and wanted to fill them in rather than leave them blank I could use the mean value shown here instead.

What I really wanted to know was the minimum and maximum for each of the four measurements by class and after a bit of digging around I came across the [`groupby`](https://realpython.com/pandas-groupby/#:~:text=You%20call%20.,a%20single%20column%20name%20to%20.) function in `pandas` which allowed me to group the classes of species and then narrow it down to show only the minimum and maximum measurements for each.  

 ![min_max_measurements](/images/min_max_measurements.png)

While not a terribly visual tool in itself, I found it useful in that it gives the range of measurements for each species and already it is clear that *Iris setosa* is smaller than the other two species. 

## Data Visualisation

### Histogram
A [histogram](https://asq.org/quality-resources/histogram) is a commonly used plotting tool to show frequency distributions in numerical data.  It visualises the distribution of values in a given dataset, the x-axis displaying the values in the dataset and the y-axis displaying the frequency of each value.  It differs from a bar chart in that it deals with quantitative data rather than categorical and elements are grouped together as ranges rather than individual entities, as they would be in a bar chart. In a histogram the data is allocated to bins, a series of intervals into which the data is effectively sorted.  Helpfully, the `pandas` in-built function `.hist()` plots histograms for the features in the dataset. In trying to establish the correct number of bins to specify I found a number of methods such as the Freedman–Diaconis rule, Sturges' rule and the Shimazaki-Shinomoto method to name but a few, and then I happened across the fact that there is an [`auto`](https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram) function, which uses the maximum of the Sturges and Freedman-Diaconis bin choice, so I quite happily deployed that instead!  It's useful to know that there are other available methods for use on future data sets though. 

I saved the four histograms to `histograms.png`.  The histograms for petal length and petal width are remarkable similar and the standalone bars to the left represent Irish Setosa, well apart from the other two species making these quite distinctive classification features. The overlap between the species in terms of sepal length and sepal width is significant such that it's not as easy to distinguish the species in these two histograms. 

 ![Histograms](/images/Histograms.png)

### Scatter plots
Scatter plots use a collection of points placed using Cartesian coordinates, basically a system used to locate a point, or points, in two-dimensional space from two variables.  By displaying a variable in each of the X and Y axis, we can clearly see if a relationship or correlation between the two variables exists. The useful thing about scatter plots is that they retain the exact data values and sample size. By colour coding the three species of iris in the plots, this distinction is even clearer. 

![Scatter Plots](/images/Scatterplots.png)

Colour coding greatly helps in interpreting these scatterplots although even without it, it would be clear that *setosa* can be easily distinguised from *versicolor* and *virginica* on all the plots. While *versicolor* and *virginica* can still be seen as fairly distinct from each other in most cases, particularly when colour coded, they nonetheless have some overlap with each other.  The notable exception to this is the scatterplot for sepal_length and sepal_width where *versicolor* and *virginica* overlap considerably.  Therefore, as classifiers between these two particular species, these are not as impactful. 

### Heatmap
A heatmap is a really powerful visualisation tool that uses colour to indicate correlation and, in my opinion, one of the most intuitive to understand.  Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to +1. Values closer to zero means there is no linear trend between the two variables.   

I used Seaborn to plot the heatmap and in order to determine the correlation I used the `.corr()` method from pandas. The closer to 1, the more positively correlated they variables are, and because this presents like a visual of the concept "hotter-colder" I chose reds for this heatmap.  Also I wanted to show the value of the cells, so I passed the parameter `annot` as True.

![Heatmap](/images/heatmap.png)

The heatmap shows that petal_length and petal_width, with a value close to 1, have a high correlation. Both petal_width and petal_length also show good correlation with sepal_length.  Sepal_width has far less relationship with petal_width and petal_length.

<a name="5.-summary-&-conclusion"></a>
## Summary & Conclusion
INSERT TEXT

<a name="6.-references"></a>
## References

Website: Iris Data Set - raw data - https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

Website: Wikipedia - Iris Flower Data Set - https://en.wikipedia.org/wiki/Iris_flower_data_set

Website: Wikipedia - Edgar Anderson - https://en.wikipedia.org/wiki/Edgar_Anderson

Website: Wikipedia - Ronald Fischer - https://en.wikipedia.org/wiki/Ronald_Fisher

Website: Wikipedia - Eugenics - https://en.wikipedia.org/wiki/Eugenics

Publication: Sweigart, A., “Automate the Boring Stuff with Python”, 2015

Blog: Stop using iris, Megal Stodal dated 24/06/2020 - https://www.meganstodel.com/posts/no-to-iris/

Blog: Discriminating Fisher's iris data by using the petal areas, Rick Wicklin on The DO Loop 09/08/2012 - https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-area

Website: Machine Learning Classification: Machine Learning with Python for Everyone, Mark Fenner dated 14/08/2019 - https://www.informit.com/articles/article.aspx?p=2982113&seqNum=2 

Website: Python – Basics of Pandas using Iris Dataset, last updated 27/08/2021 - https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

Website: Machine Learning with Iris Dataset, Anand Venkataraman dated 2019 -  https://www.kaggle.com/sixteenpython/machine-learning-with-iris-dataset

Website: Pandas Dataframe Describe Method - https://www.w3schools.com/python/pandas/ref_df_describe.asp

Website: Yet Another Iris EDA, Aditya Jetely,  dated 12/10/2020 - https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d

Website: Stack overflow: How to choose bins in matplotlib histogram - https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram

Website: Datacamp: plotting a histogram of iris data - https://www.datacamp.com/community/tutorials/histograms-matplotlib

Website: Visualizing Data in Python Using plt.scatter() - https://realpython.com/visualizing-python-plt-scatter/

Website: Heatmap interpretation, dated February 2019 - https://stats.stackexchange.com/questions/392517/how-can-one-interpret-a-heat-map-plot


<!-- Acknowledgements -->
## Acknowledgements:
