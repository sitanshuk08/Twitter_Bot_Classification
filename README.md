# Twitter Bot Classification
### Team_Members: 
##### Isha Goyal 
##### Nayanika Bisht 
##### Sitanshu Kumar
### Domain: Machine Learning
##### Use of bots in artificially elevating certain issues on social media

### Problem_Statement: 
##### In the time of internet, when social media is used to elevate problems of many. Organisations are using bots to artiificially increase the social media presence of topics and posts that help them. This may be a problem  

### Reference Work:
##### https://www.pewresearch.org/internet/wp-content/uploads/sites/9/2018/04/PI_2018.04.09_Twitter-Bots_FINAL.pdf
##### Summary: https://www.pewresearch.org/internet/2018/04/09/bots-in-the-twittersphere/

##### https://botometer.iuni.iu.edu/#!/
##### https://core.ac.uk/download/pdf/237398342.pdf
##### https://science.sciencemag.org/content/359/6380/1146.full

##### Google doc for summary and key takeaways:

##### Google doc for summary and key takeaways (Nayanika): https://docs.google.com/document/d/17g36Qs5qLrHx_KK6EoTt5iSeqtA2QioTqRpiIEZWUoA/edit
##### Google doc for summary and key takeaways (Isha): https://docs.google.com/document/d/1gJdi4KgQt34TlEM67sF-nZWESHRdiLqoA9nXdxJ704U/edit
##### Google doc summary of the Summary and key takeaways (Sitanshu): https://docs.google.com/document/d/1XVk-tJ_BCr5eNHcXQePiczPIyKwqN5y2uHl-IbZhTZk/edit?usp=sharing

### Data: To be scraped from twitter based on topics trending.
###### We have (for now) decided to use trending topics using hashtags as the likelihood of bots being employed is higher. In case of political viewpoints, we will take opposing views together to assess if either of the trend is more likely to be artificially elevated.
###### Link to the google sheet with basic info about extracted tweets: https://docs.google.com/spreadsheets/d/1w3rFa2pzfRUg9t5VpGKMv_Fmw2TMpofLoF9PO7dZCyQ/edit?usp=sharing


### Software: Python
### Statistical Techniques
##### Logistics Regression for classification of Accounts into automated and genuine account
##### Synthetic Minority Oversampling Technique (SMOTE) and Near Miss algorithm for oversampling and undersampling to create a balanced training data
##### 

### Methodology
##### Running regression model on CRESCI data to understand how to fit a model to the data.
###### import required libraries (numpy and pandas)
###### reading the data file
###### cleaning the dataset and processing the data to desired include desired variable, we have included following variables.


### Questions to be answered:
#### What libraries are we going to use?
###### We are using following libraries:
###### Tweepy to collect data from twitter
###### Pandas to manuplate dataframe
###### imbalanced-learn for SMOTE and near miss algorithm
###### sklearn for conducting logistic regression regression
###### matplotlib.pyplot to create plots to undersatand the fit
#### What will we do the text data and how?
###### Not decided yet
#### How will we generate variables/features?
###### Currently, based on certain research papers, we are using variables already provided in them currently and want to asses the accuracy of the model built on those variables.
###### When we extract tweets from twitter, we are able to extract certain features of the tweet itself along with the user who tweeted it. For now we are going to study the user and not the tweet itself when deciding if the user is automated or not.
###### 

