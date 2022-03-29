# pands-project
## Project to analyse the iris data set


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Introduction">Introduction</a></li>
    <li><a href="#Technical-Specification">Technical Specifications</a></li> 
    <li><a href="#The-Fisher-Iris-Data-Set">The Fisher Iris Data Set</a></li>
    <ul>
        <li><a href="#History">History</a></li>
        <li><a href="#Relationship">Relationship With Machine Learning</a></li>
      </ul>
    </li>
    <li><a href="#Investigation">My Investigation of the Data Set Using Python</a></li>
    <li><a href="#Summary-&-Conclusion">Summary & Conclusion</a></li>
    <li><a href="#References">References</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- Introduction -->
## Introduction

This repository contains my pands project on the Fischer Iris Data Set, submitted for assessment under the Programming and Scripting module which in turn forms part of the Higher Diploma in Computing and Data Analytics at GMIT.

In this project I will outline the programs and tools used to build and execute this project before covering the history and provenance of the Fischer iris data set and why it is so widely used in machine learning. 

I will be using VS Code as my source code editor and this accompanying README file outlines the thinking behind coding which I use to introduce, manipulate and present the data therein, discussion of the code used to examine and manipulate the data set, generate informative plots and visualisations from that data and finally summarise my findings and conclusions.

The aim and purpose of this project is to improve upon my Python coding and scripting, learn more about the dynamics of machine learning and the functions and uses of data visualisations. 

 
<!-- Technical Specifications -->
## Technical Specifications

### How to Download this project

1. Go to the URL for the repository on GitHub at [https://github.com/Scunnies/pands-project.git](https://github.com/Scunnies/pands-project.git))
2. Click the green `Code` button
3. You now have the option to either clone the repository, open with [Github Desktop](https://desktop.github.com/) or download the zip file
 

<!-- The Fisher Iris Data Set -->
## The Fisher Iris Data Set – History and Relationship with Machine Learning
<!-- History -->
### History
The [Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) represents four measurements of floral morphology on 150 plants - 50 individuals for each of three genus (I. versicolor, I. setosa, and I. virginica).  The numeric parameters which the dataset contains are Sepal width, Sepal length, Petal width and Petal length. With the exception of one or two points, the classes are linearly separable and, as a result, classification algorithms reach almost perfect accuracy.  Classification accuracy is the ratio of number of correct predictions to the total number of input samples, it works best if there are equal number of samples belonging to each class.

It was, in fact, [Edgar Shannon Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) (1897 - 1969) who collected the data to quantify the structural variation of Iris flowers of three related species, providing the raw data which formed the basis of the famous iris data set.  His research was focused on developing techniques to quantify geographic variation in Iris versicolor. It was, in fact, Anderson who determined the existence of a second species, Iris virginica.  It was during the 1930’s as part of this reasearch that Anderson gathered and documented the dataset which forms the basis of this and no doubt thousands of other machine learning assignments.  In 1929 Anderson received a fellowship to undertake studies at the John Innes Horticultural Institute in Britain, where he worked with cytogeneticist C. D. Darlington, geneticist J. B. S. Haldane and most notably for the purposes of this assignment, statistician R. A. Fisher.  If I were to correlate the Iris data set to Band Aid then Anderson was Midge Ure to Fisher's Geldof, in as much as he gets credited only occasionally!

The Geldof of their relationship was [Sir Ronald Aylmer Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) (1890 – 1962), a British mathematician, statistician, geneticist and academic. For his work in statistics, he has been variously described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics" and was touted as a natural successor to Darwin in terms of his scientific and evolutionary theorising.  Notwithstanding his genius, Fisher had some questionable links to [eugenics](https://en.wikipedia.org/wiki/Eugenics), he was a founding Chairman of the University of Cambridge Eugenics Society in 1911.  Eugenics is a set of beliefs and practices that aim to improve the genetic quality of a human population, historically by excluding people and groups judged to be inferior or promoting those judged to be superior.  Fischer went on to distance himself from the society in 1941 but then, subsequent to World War II, wrote a character reference for a Nazi eugenicist who had inauspicious links to Josef Mengele.   His paper on the Iris data set, which was published in 1936, has been accused of being a tool to advance the science of eugenics, proposing a methodological framework to delineate 'desirable' traits, ostensibly to promote eugenics programs. This is one reason why other data sets are often ushered forth as more morally palatable substitutes.  Alternatives, as suggested by one Data Scientist, [Megan Todal](https://www.meganstodel.com/posts/no-to-iris/), include data on cars (`mpg` from `ggplot2`), hawks (found in the `Stat2Data` package) and mushrooms (data set available on the Machine Learning Repository of the UC Irvine website).   

<!-- Relationship -->
### Relationship with Machine Learning
Each row in the Iris dataset describes one flower for which there are four seperate measurements - the length and width of the sepals, the length and width of the petals.  The 5th column is the species of iris: setosa, versicolor, or virginica. Sepals (because I had to look them up!) serve as protection for the flower in bud and often as support for the petals when in bloom.

Despite its shaky provenance the Fisher data set is described as the 'Hello World' for machine learning, useful for practicing basic machine learning algorithms.  It endures because the data is open source, the accuracy and origin are both known, and with three types of flower, it allows for more than just binary classification.  Additionally, with an even 50 in each classification it is balanced and has no null or missing values.  All measurements are on the same scale (cm) so no normalisation is called for and the file size isn’t unwieldy or excessively complicated.  


<!-- Investigation -->
## My Investigation of the Data Set Using Python
My first step was to import the libaries that I felt would be most useful in manipulating the data.  The are as follows:
`numpy` - short for Numerical Python and used to perform a wide variety of mathematical operations on arrays
`pandas` - for data manipulation and analysis with data structures and operations for manipulating numerical tables and time series
`matplotlib.pyplot` - a plotting library for creating static, animated, and interactive visualizations in Python
`seaborn` -  based on matplotlib, this data visualization library provides a high-level interface for drawing attractive and informative statistical graphics
`re` - [NOTE TO SELF: NOT SURE I WILL USE THIS?]

Next I imported the data set from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) as iris.csv and read it in and did a quick print check to ensure it was working as intended

`data = pd.read_csv('iris.csv')`
`print (iris)`

This data set being quite small, very famous and scrutinised to death I already know that the data is ship shape for analysis and doesn't require any tidy-up but it seems also to be good practice when dealing with data to check for null values as a program encountering a null value may return an error.  Missing values are usually represented in the form of Nan, null or None.  

Having been down a rabbit hole on this subject, I understand there are many ways to deal with missing/null values but it depends on the type of data set in question.  For argument's sake, had I encountered null values in this particular data set I likely would have used the median value to replace them and we will see how that is calculated further on. 

Summary of each variable, output to a text file

Histogram of each variable, output to a png file
[calculation of bins](https://www.datacamp.com/community/tutorials/histograms-matplotlib)



<!-- SummaryConclusion -->
## Summary & Conclusion
INSERT TEXT

<!-- References -->
## REFERENCES:

The Fisher Iris Data Set – History and Relationship with Machine Learning:
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://en.wikipedia.org/wiki/Eugenics
https://en.wikipedia.org/wiki/Ronald_Fisher
https://en.wikipedia.org/wiki/Edgar_Anderson
https://www.meganstodel.com/posts/no-to-iris/
https://www.informit.com/articles/article.aspx?p=2982113&seqNum=2 # 3.2 A Simple Classification Dataset, Machine Learning with Python for Everyone 
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://www.kaggle.com/sixteenpython/machine-learning-with-iris-dataset

https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d

Datacamp: plotting a histogram of iris data https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5
https://www.datacamp.com/community/tutorials/histograms-matplotlib

Trying to find something interesting I can do with the data:
https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-areas.html

Research on classification accuracy:
https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234

ReadMe template:
https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/BLANK_README.md

<!-- Acknowledgements -->
## Acknowledgements:
