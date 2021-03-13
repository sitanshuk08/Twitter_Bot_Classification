# Twitter Bot Classification
### Team_Members:
##### Isha Goyal
##### Nayanika Bisht
##### Sitanshu Kumar
### Domain: Machine Learning
##### Primary: Use of bots in artificially elevating certain issues on social media
###### Secondary: Identifying bots based on prior classification based on research papers.

### Problem_Statement: 
##### In the time of internet, when social media is used to elevate problems of many. Organisations are using bots to artiificially increase the social media presence of topics and posts that help them. This may be a problem  

### Reference Work:
##### https://www.pewresearch.org/internet/wp-content/uploads/sites/9/2018/04/PI_2018.04.09_Twitter-Bots_FINAL.pdf
##### Summary: https://www.pewresearch.org/internet/2018/04/09/bots-in-the-twittersphere/

##### https://botometer.iuni.iu.edu/#!/
##### https://core.ac.uk/download/pdf/237398342.pdf
##### https://science.sciencemag.org/content/359/6380/1146.full

##### Google doc for summary and key takeaways:
https://docs.google.com/document/d/1vd5kVM37eidYJXnUK3_SNztA0aYqo3kZJeJnXLVBLeE/edit?usp=sharing

##### Google doc for summary and key takeaways (Nayanika): https://docs.google.com/document/d/17g36Qs5qLrHx_KK6EoTt5iSeqtA2QioTqRpiIEZWUoA/edit
##### Google doc for summary and key takeaways (Isha): https://docs.google.com/document/d/1gJdi4KgQt34TlEM67sF-nZWESHRdiLqoA9nXdxJ704U/edit
##### Google doc summary of the Summary and key takeaways (Sitanshu): https://docs.google.com/document/d/1XVk-tJ_BCr5eNHcXQePiczPIyKwqN5y2uHl-IbZhTZk/edit?usp=sharing

### Data: To be scraped from twitter based on topics trending and CRESCI data set (Prior classified data for training purpose.
##### We have (for now) decided to use trending topics using hashtags as the likelihood of bots being employed is higher. In case of political viewpoints, we will take opposing views together to assess if either of the trend is more likely to be artificially elevated.
##### Link to the google sheet with basic info about extracted tweets: https://docs.google.com/spreadsheets/d/1w3rFa2pzfRUg9t5VpGKMv_Fmw2TMpofLoF9PO7dZCyQ/edit?usp=sharing
##### Training data: Cresci
###### traditional spambots 4: job and job related offering profiles
###### traditional spambots 3: dormant account, last active around 2011
###### traditional spambots 2: prize money, lottery accounts
###### traditional spambots 1: without profile image

### Software: Python
### Statistical Techniques
##### Exploratory Data Analysis for understanding bot/spam behavior and using the same on our data.
##### Transformation of Categorical Data for further analysis
##### Transforming the data to deal with skewness and outliers
##### Logistics Regression for classification of Accounts into automated and genuine account
##### Synthetic Minority Oversampling Technique (SMOTE) and Near Miss algorithm for oversampling and undersampling to create a balanced training data
##### Standardisation or Normalisation for scaling of variables
##### Cross Validation

### Methodology
Data preprocessing: na values and removing variables
Understanding the data
Using one hot encoding for categorical data transformation
Standardisation or Normalisation
Logistic Regression on Variables:
SMOTE and Near Miss
Confusion Matrix:
Accuracy
Precision
Recall
F1 Score
Cross Validation

### Questions to be answered:
#### What libraries are we going to use?
###### We are using following libraries:
###### Tweepy to collect data from twitter
###### Pandas to manuplate dataframe
###### imbalanced-learn for SMOTE and near miss algorithm
###### sklearn for conducting logistic regression regression, scaling the variables and cross validation
###### matplotlib.pyplot to create plots to undersatand the fit
#### What will we do the text data and how?
###### Not decided yet
#### How will we generate variables/features?
###### Currently, based on certain research papers, we are using variables already provided in them currently and want to asses the accuracy of the model built on those variables.
###### When we extract tweets from twitter, we are able to extract certain features of the tweet itself along with the user who tweeted it. For now we are going to study the user and not the tweet itself when deciding if the user is automated or not.
###### 



## Meeting 3 
##### Data Dictionary: https://docs.google.com/document/d/1GTVCl7X848DRhEv8OSf59kfoBl-k3z8H7o3CFs2lm5U/edit 

#### Questions raised:

######    How to correctly treat the categorical data in a data frame?

###### How to deal with independent but correlated data? In general, what are the impacts of violation of assumption of model on data and how to treat them effectively?
####### Multicollinearity only a problem for the variables that are collinear. It increases the standard errors of their coefficients, and it may make those coefficients unstable in several ways.
####### Variance Inflation Factor [VIF]: estimates how much the variance of a coefficient is “inflated” because of linear dependence with other predictors i.e. high VIF implies multicollinearity
####### Situations where high VIFs can be ignored:
####### 1. Variables with high VIFs are control variables, and the variables of interest do not have high VIFs
####### 2. High VIFs are caused by the inclusion of powers or products of other variables
####### 3. Variables with high VIFs are indicator (dummy) variables that represent a categorical variable with three or more categories

###### Log transformation and it’s limitation:

###### Box Plot and it’s limitation:

######    Works with quantile and is highly dependent on second moments

###### Skewness and Kurtosis of data can not be quantified. Specifically, kurtosis.

######    Univariate Analysis and may result in wrong conclusions


###### ** Read about Robustness library in R, Adjusted Box plot help document and the research paper included in it.

###### Read about Box-Cox transformation.

###### Statistics that allows us to test the categorical variables.

###### State the hypothesis clearly in notebook.




