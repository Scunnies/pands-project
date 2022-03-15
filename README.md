# pands-project
## Project to analyse the iris data set

Table of Contents 

Introduction

Technical Specifications

The Fisher Iris Data Set – History and Relationship with Machine Learning

My Investigation of the Data Set Using Python

Summary and Conclusion

References

 
## Introduction

This repository contains my pands project on the Fischer Iris Data Set, submitted for assessment under the Programming and Scripting module which in turn forms part of the Higher Diploma in Computing and Data Analytics at GMIT.

In this project I will outline the programs and tools used to build and execute this project before covering the history and provenance of the Fischer iris data set and why it is so widely used in machine learning. I will use Python programming to examine and manipulate the data set and generate informative plots and visualisations from that data and finally summarise my findings and conclusions.

The aim and purpose of this project is to improve upon my Python coding and scripting, learn more about the dynamics of machine learning and the functions and uses of data visualisations. 

 
## Technical Specifications
I will be using VS Code as my source code editor and this accompanying README file provides an introduction to the history of the Iris data set, outlines the thinking behind coding which I use to introduce, manipulate and present the data therein, discussion of the code and what it is expected to do, plotting various visual outcomes which are hopefully both informative and attractive.

[Python / programs / how to download, use and run]
 

## The Fisher Iris Data Set – History and Relationship with Machine Learning
The Fischer Iris Data Set represents four measurements of floral morphology on 150 plants - 50 individuals for each of three genus (I. versicolor, I. setosa, and I. virginica).  The numeric parameters which the dataset contains are Sepal width, Sepal length, Petal width and Petal length. With the exception of one or two points, the classes are linearly separable and, as a result, classification algorithms reach almost perfect accuracy.

It was, in fact, Edgar Shannon Anderson [INSERT DATES] who provided the raw data which formed the basis of the famous iris data set.  In the 1930’s as part of his research to quantify geographic variation in Iris versicolor, Anderson gathered and documented the dataset which forms the basis of this and no doubt thousands of other machine learning assignments.   Anderson happened to be a fellow at the John Innes Horticultural Institute in Britain, where he worked alongside statistician R. A. Fisher and it was Fisher who used Anderson's data set to demonstrate statistical methods of classification.   The data set is very well known in the machine learning community and more usually, and a little unfairly, known as Fisher's iris data set. If this data set were compared to Band Aid then Anderson was Midge Ure to Fischer's Geldof!

Sir Ronald Aylmer Fisher (1890 – 1962) was a British mathematician, statistician, geneticist, and academic. For his work in statistics, he has been variously described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics" and was touted as a natural successor to Darwin in terms of his scientific theorising.  Notwithstanding his genius, Fisher had some questionable links to eugenics, having been a founding Chairman of the University of Cambridge Eugenics Society in 1911.  He went on to distance himself from the society in 1941 but then, subsequent to World War II, wrote a character reference for a Nazi eugenicist who had inauspicious links to Josef Mengele.   His paper on the Iris data set, which was published in 1936, has been accused of being a tool to advance the science of eugenics, and this is one reason why other data sets are often ushered forth as more morally palatable substitutes.  Alternatives include data on cars (`mpg` from `ggplot2`), hawks (found in the `Stat2Data` package) and mushrooms (data set available on the Machine Learning Repository of the UC Irvine website).   As I understand it, the Fisher data set endures because the data is open source, the accuracy and origin are both known, and with three types of flower, it allows for more than just binary classification.  With an even 50 in each classification it is balanced and the file size isn’t unwieldy or excessively complicated.

I know I’m not going to re-invent the wheel here but I hope at least to come up with some visually pleasing graphs and interesting observations.

 

 

 

https://en.wikipedia.org/wiki/Iris_flower_data_set

https://www.meganstodel.com/posts/no-to-iris/

https://www.kaggle.com/sixteenpython/machine-learning-with-iris-dataset

https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d