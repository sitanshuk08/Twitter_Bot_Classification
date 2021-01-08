#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("/home/lenovo/Downloads/Hunger_Games/cresci_final_data.csv")
df  = df.drop(labels = "Unnamed: 0", axis=1)

#followers count
df.loc[df["followers_count"] > 999, "follower >999"] = "1"
df.loc[df["followers_count"] < 999, "follower >999"] = "0"

#absence of profile picture
#df.loc[df[""]]


#user has "en" as defaut language of the account 
df.loc[df["lang"] = "en", "language = en"] = "1"
df.loc[df["lang"] != "en", "language = en"] = "0"

#less than 50 tweets
df.loc[df["statuses_count"] < 50, "less than 50 tweets"] = "1"
df.loc[df["statuses_count"] >= 50, "less than 50 tweets"] = "0"

#description contains url
df.loc[df["description"].str.contains("www.", na = False), "contains_url"] = "1"
df.loc[df["contains_url"] != "1", "contains_url"] = "0"

#friends follower ratio
df["friends follower ration"] = df["friends_count"]/df["followers_count"]

df.loc[df["friends follower ratio"] > 2, "friends_follower_ratio > 2:1"] = 1
df.loc[df["friends follower ratio"] < 2, "friends_follower_ratio > 2:1"] = 0

df.loc[df["friends follower ratio"] > 50, "friends_follower_ratio > 50:1"] = 1
df.loc[df["friends follower ratio"] < 50, "friends_follower_ratio > 50:1"] = 0

df.loc[df["friends follower ratio"] > 100, "friends_follower_ratio > 100:1"] = 1
df.loc[df["friends follower ratio"] < 100, "friends_follower_ratio > 100:1"] = 0

#absence of profile picture
df.loc[df["profile_image_url"] == "", "absence_of_profile_image"] = 1
df.loc[df["profile_image_url"] != "", "absence_of_profile_image"] = 0


#has less than 30 followers
df.loc[df["followers_count"] < 30, "follower < 30 "] = "1"
df.loc[df["followers_count"] >= 30, "follower < 30"] = "0"

#not geo located

df.loc[df["geo_enabled"] == "", "geo_location"] = "0"
df.loc[df["geo_enabled"] != "", "geo_location"] = "1"


#age of account
df['year'] = pd.DatetimeIndex(df['timestamp']).year
from datetime import date
today = date.today()
today
df['age']=today.year-df['year']
#lists per user
df['listsperuser']=df["listed_count"]

#user favourites
df['user_fav']=df['favourites_count']

#default profile image
df.loc[df["default_profile_image"] != "", "default_profileimg"] = "0"
df.loc[df["default_profile_image"] == 1, "default_profileimg"] = "1"

#description presence
df.loc[df["description"] == "", "description_presence"] = "0"
df.loc[df["description"] != "", "descritption_presence"] = "1"

df.to_csv("/home/lenovo/Downloads/Hunger_Games/cresci_processed_data.csv")

