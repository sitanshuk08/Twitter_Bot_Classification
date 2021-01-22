#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the data and required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sn
df=pd.read_csv("C:\\Users\\nayan\\OneDrive\\Desktop\\bots\\finaldata.csv")


# In[2]:


# inspecting the data
df.shape


# In[3]:


# checking the first few rows of the dataset to see what we're dealing with
df.head()


# In[4]:


#dropping redundant and deprecated variables 
df = df.drop(["url","lang","geo_enabled","time_zone","location","profile_image_url","profile_banner_url","profile_use_background_image","profile_background_image_url_https","profile_text_color","profile_image_url_https","profile_sidebar_border_color","profile_background_tile","profile_sidebar_fill_color","profile_background_image_url","profile_background_color","profile_link_color","utc_offset","is_translator","follow_request_sent","notifications","description","contributors_enabled","following","created_at","timestamp","crawled_at","updated","random","testset"], axis = 1)


# In[5]:


# manipulating target variable by putting 0 and 1 values
df.loc[df["Category"] == 'genuine', "class"] = "0"
df.loc[df["Category"] != 'genuine', "class"] = "1"
df = df.drop(["Category"], axis = 1)


# In[6]:


# checking missingness in variables
df.isnull().mean().sort_values()


# In[7]:


# putting missing values as 0 in default_profile, protected, default_profile_image and verified columns
df["default_profile"] = df["default_profile"].fillna(0)
df["protected"] = df["protected"].fillna(0)
df["default_profile_image"] = df["default_profile_image"].fillna(0)
df["verified"] = df["verified"].fillna(0)


# In[8]:


# confirming there are no nulls except in name
df.isnull().mean()


# In[9]:


# checking the data type of each variable
df.dtypes


# In[10]:


# converting default_profile, default_profile_image, protected, verified and class to boolean
df["default_profile"] = df["default_profile"].astype("bool")
df["default_profile_image"] = df["default_profile_image"].astype("bool")
df["protected"] = df["protected"].astype("bool")
df["verified"] = df["verified"].astype("bool")
df["class"] = df["class"].astype("bool")
df.dtypes


# In[11]:


# checking for duplicate values on the basis of all columns
duplicate = df[df.duplicated()]
duplicate


# In[12]:


# checking for duplicate values on the basis of screen name
duplicate = df[df.duplicated('screen_name')]
duplicate


# In[13]:


# dropping duplicate values on basis of screen name
df.drop_duplicates(subset ="screen_name", 
                     keep = False, inplace = True)
df
# no rows have been dropped


# In[14]:


# dropping duplicates on basis of all columns
df.drop_duplicates(keep=False,inplace=True)
df.round(0)
df
# no rows have been dropped


# In[15]:


# exporting cleaned data
df.to_excel(r'C:\\Users\\nayan\\OneDrive\\Desktop\\bots\\data_cleaned.xlsx')


# In[16]:


# Descriptive statistics
pd.options.display.float_format = '{:.5f}'.format
df.describe()


# In[17]:


corrMatrix = df.corr()
sn.heatmap(corrMatrix, vmin=-1, vmax=1, center=0,
    cmap=sn.diverging_palette(20, 220, n=200),
    square=True)
sn.set(rc={'figure.figsize':(19,19)})
sn.set(font_scale = 6)
pyplot.show


# In[18]:


sn.set(rc={'figure.figsize':(15,15)})
sn.set(font_scale = 3)
sn.boxplot(y= df["statuses_count"])


# In[19]:


fig, ax = pyplot.subplots(figsize=(16,8))
ax.scatter(df['friends_count'], df['followers_count'])
ax.set_xlabel('Friends')
ax.set_ylabel('Followers')
ax.ticklabel_format(style = 'plain')
pyplot.show()


# In[20]:


fig, ax = pyplot.subplots(figsize=(16,8))
ax.scatter(df['favourites_count'], df['statuses_count'])
ax.set_xlabel('Favourites')
ax.set_ylabel('Statuses')
ax.ticklabel_format(style = 'plain')
pyplot.show()


# In[21]:


fig, ax = pyplot.subplots(figsize=(16,8))
ax.scatter(df['listed_count'], df['followers_count'])
ax.set_xlabel('Listed')
ax.set_ylabel('Followers')
ax.ticklabel_format(style = 'plain')
pyplot.show()


# In[22]:


fig, ax = pyplot.subplots(figsize=(16,8))
ax.scatter(df['listed_count'], df['friends_count'])
ax.set_xlabel('Listed')
ax.set_ylabel('Friends')
ax.ticklabel_format(style = 'plain')
pyplot.show()

