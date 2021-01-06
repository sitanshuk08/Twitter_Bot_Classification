#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import tweepy as tw
import pandas as pd

from tweepy import Stream



from tweepy import OAuthHandler
from tweepy import API

# Consumer key authentication(consumer_key,consumer_secret can be collected from our twitter developer profile)
auth = OAuthHandler(consumer_key, consumer_secret)

# Access key authentication(access_token,access_token_secret can be collected from our twitter developer profile)
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth, wait_on_rate_limit = True, retry_delay = 30, retry_count= 10)

search_words = "#योगीजी_नंबर_01"
date_since = "2021-01-02"

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items()
json_data = [r._json for r in tweets]
df_tweet = pd.json_normalize(json_data)

df_tweet.to_csv("/home/lenovo/Documents/project_twitter/tweet_data_3.csv")


# In[ ]:




