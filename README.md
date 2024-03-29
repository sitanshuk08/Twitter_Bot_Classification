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
EDA to better understand the data
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
###### sklearn and statsmodel.api for conducting logistic regression regression, scaling the variables and cross validation
###### matplotlib.pyplot to create plots to undersatand the fit
###### sklearn for crossvalidation, randomforestclassifier, 

#### What will we do the text data and how?
###### Not decided yet

#### How will we generate variables/features?
###### Based on certain research papers, we are using variables already provided and asses the accuracy of the model built on those variables.
###### We observed high accuracy based on limited variables on our data and hence feel that adding more variables may lead to the problem of overfitting. Would like to fit the real world data before commenting on adding more features.

###### When we extract tweets from twitter, we are able to extract certain features of the tweet itself along with the user who tweeted it. For now we are going to study the user and not the tweet itself when deciding if the user is automated or not.


## Meeting 3 
##### Data Dictionary: https://docs.google.com/document/d/1GTVCl7X848DRhEv8OSf59kfoBl-k3z8H7o3CFs2lm5U/edit 

#### Questions raised:

##### How to correctly treat the categorical data in a data frame?
###### The following link mentions few ways to deal with the categorical data:
        https://towardsdatascience.com/understanding-feature-engineering-part-2-categorical-data-f54324193e63
###### Strictly speaking label encoding for nominal data and One hot Encoding Scheme is used to label n levels of categorical variable into n-1 indicator variables which can be fitted in regression model. There are other methods like Ordinal Encoding, Dummy Coding scheme, effect coding scheme and Feature Hasher. 

##### How to deal with independent but correlated data? In general, what are the impacts of violation of assumption of model on data and how to treat them effectively?
###### Multicollinearity only a problem for the variables that are collinear. It increases the standard errors of their coefficients, and it may make those coefficients unstable in several ways.
###### Variance Inflation Factor [VIF]: estimates how much the variance of a coefficient is “inflated” because of linear dependence with other predictors i.e. high VIF implies multicollinearity
###### Situations where high VIFs can be ignored:
###### 1. Variables with high VIFs are control variables, and the variables of interest do not have high VIFs
###### 2. High VIFs are caused by the inclusion of powers or products of other variables
###### 3. Variables with high VIFs are indicator (dummy) variables that represent a categorical variable with three or more categories


##### Log transformation and it’s limitation:

##### Box Plot and it’s limitation:
######  Works with quantile and is highly dependent on second moments
######  Skewness and Kurtosis of data can not be quantified. Specifically, kurtosis.
######  Univariate Analysis and may result in wrong conclusions


##### ** Read about Robustness library in R, Adjusted Box plot help document and the research paper included in it.

###### Since the original Boxplot is based on normal data, at times in case of skewed data boxplot may suggest wrong classification. Research was done in this regard and Medcouple and other statistics were developed.  

###### Read about Box-Cox transformation.
###### A Box Cox transformation is a transformation of a non-normal dependent variables into a normal shape. https://towardsdatascience.com/box-cox-transformation-explained-51d745e34203 This article depicts how this transformation changes a non normal distribution to look something like a Normal Distribution.

##### Statistics that allows us to test the categorical variables.
###### We use chi-square to test for independence of the features using contingency tables. Also, we can use Wald's statistic to test whether a feature is significant to the model, but this step is after fitting the model.

###### State the hypothesis clearly in notebook.

## Meeting 4

##### Primary tasks

###### Making use of one hot encoding for data transformationn of categorical variable.
###### Use of chi square test statistics for independence of attributes
###### https://towardsdatascience.com/how-to-test-for-statistically-significant-relationships-between-categorical-variables-with-chi-66c3ebeda7cc
###### What would be the ideal workflow, from this point onwards?
###### 








### Reference and other docs created while working on the project.
##### https://www.pewresearch.org/internet/wp-content/uploads/sites/9/2018/04/PI_2018.04.09_Twitter-Bots_FINAL.pdf
##### Summary: https://www.pewresearch.org/internet/2018/04/09/bots-in-the-twittersphere/
##### https://botometer.iuni.iu.edu/#!/
##### https://core.ac.uk/download/pdf/237398342.pdf
##### https://science.sciencemag.org/content/359/6380/1146.full



##### Google doc for summary and key takeaways: https://docs.google.com/document/d/1vd5kVM37eidYJXnUK3_SNztA0aYqo3kZJeJnXLVBLeE/edit?usp=sharing
##### Google doc for summary and key takeaways (Nayanika): https://docs.google.com/document/d/17g36Qs5qLrHx_KK6EoTt5iSeqtA2QioTqRpiIEZWUoA/edit
##### Google doc for summary and key takeaways (Isha): https://docs.google.com/document/d/1gJdi4KgQt34TlEM67sF-nZWESHRdiLqoA9nXdxJ704U/edit
##### Google doc summary of the Summary and key takeaways (Sitanshu): https://docs.google.com/document/d/1XVk-tJ_BCr5eNHcXQePiczPIyKwqN5y2uHl-IbZhTZk/edit?usp=sharing






