#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DATA INSPECTION & CLEANING


# In[2]:


# importing the data and required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sn
df=pd.read_csv("C:\\Users\\nayan\\OneDrive\\Desktop\\bots\\finaldata.csv")


# In[3]:


# inspecting the data
df.shape


# In[4]:


# checking the first few rows of the dataset to see what we're dealing with
df.head()


# In[5]:


#dropping redundant and deprecated variables 
df = df.drop(["location","utc_offset","is_translator","follow_request_sent","notifications","description","contributors_enabled","following","created_at","timestamp","crawled_at","updated","random","testset"], axis = 1)
df


# In[6]:


# manipulating target variable by putting 0 and 1 values
df.loc[df["Category"] == 'genuine', "class"] = "0"
df.loc[df["Category"] != 'genuine', "class"] = "1"
df = df.drop(["Category"], axis = 1)
df


# In[7]:


# checking missingness in variables
df.isnull().mean().sort_values()


# In[8]:


# putting missing values as 0 in default_profile, protected, default_profile_image and verified columns
df["default_profile"] = df["default_profile"].fillna(0)
df["protected"] = df["protected"].fillna(0)
df["default_profile_image"] = df["default_profile_image"].fillna(0)
df["verified"] = df["verified"].fillna(0)
df["geo_enabled"] = df["geo_enabled"].fillna(0)
df["profile_background_tile"] = df["profile_background_tile"].fillna(0)
df["profile_use_background_image"] = df["profile_use_background_image"].fillna(0)


# In[9]:


# confirming there are no nulls except in name
df.isnull().mean().sort_values()


# In[10]:


# checking the data type of each variable
df.dtypes


# In[11]:


# converting required variables to boolean
df["default_profile"] = df["default_profile"].astype("bool")
df["default_profile_image"] = df["default_profile_image"].astype("bool")
df["protected"] = df["protected"].astype("bool")
df["verified"] = df["verified"].astype("bool")
df["geo_enabled"] = df["geo_enabled"].astype("bool")
df["profile_use_background_image"] = df["profile_use_background_image"].astype("bool")
df["profile_background_tile"] = df["profile_background_tile"].astype("bool")
df["class"] = df["class"].astype("float64")
df.dtypes


# In[12]:


df["class"] = df["class"].astype("bool")
df.dtypes


# In[13]:


df


# In[14]:


# checking for duplicate values on the basis of all columns
duplicate = df[df.duplicated()]
duplicate


# In[15]:


# checking for duplicate values on the basis of screen name
duplicate = df[df.duplicated('screen_name')]
duplicate


# In[16]:


# dropping duplicate values on basis of screen name
df.drop_duplicates(subset ="screen_name", 
                     keep = False, inplace = True)
df
# no rows have been dropped


# In[17]:


# dropping duplicates on basis of all columns
df.drop_duplicates(keep=False,inplace=True)
df.round(0)
df
# no rows have been dropped


# In[18]:


# exporting cleaned data
df.to_csv(r'C:\\Users\\nayan\\OneDrive\\Desktop\\bots\\data_cleaned.csv')


# In[19]:


# EDA


# In[20]:


import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import gc
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import pylab as py 
import statsmodels.api as sm


# In[ ]:


df_test = pd.read_csv(r"C:\\Users\\nayan\\OneDrive\\Desktop\\bots\\data_cleaned.csv")
df_test = df_test.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1)
df = df_test


# In[ ]:


df = df[['id', 'screen_name', 'statuses_count', 'followers_count', 'friends_count', 'favourites_count', 'listed_count', 'default_profile', 'default_profile_image', 'protected', 'verified', 'class']]


# In[ ]:


list = [['default_profile', 'default_profile_image', 'protected', 'verified', 'class']]
for i in list:
    df[i] = df[i].astype('category')


# In[ ]:


df.info()


# In[ ]:


pd.options.display.float_format = '{:.5f}'.format
df.describe()


# In[ ]:


corrMatrix = df.corr()
sns.set(rc = {'figure.figsize':(10, 10)} )
sns.set(font_scale = 2)
sns.heatmap(corrMatrix, vmin = -1, vmax = 1, center = 0, cmap = sns.diverging_palette(20, 220, n = 200), square = True, cbar_kws = {'shrink': 0.6}, annot = True)
plt.show


# In[ ]:


df.info()


# In[ ]:


list = ['statuses_count', 'followers_count', 'friends_count', 'favourites_count', 'listed_count']
for i in list:
    fig = plt.figure(figsize =(7, 7)) 
    # Creating axes instance 
    ax = fig.add_axes([1, 1, 1, 1]) 
    #change of origin by adding 1 to the original data 
    ax.boxplot(np.log(df[i] + 1 ))


# In[ ]:


list = {'statuses_count', 'followers_count', 'friends_count', 'favourites_count', 'listed_count'}
for i in list:
    fig, ax = plt.subplots(1)
    sns.histplot(df[i]+1, bins = 100, log_scale= True, kde = True)
    #np.log(df[i]+1).plot.hist(bins = 100)


# In[ ]:


from scipy import stats


# In[ ]:


type(df['statuses_count'])


# In[ ]:


#look for details
crim_boxcox = stats.boxcox(df['statuses_count']+1)[0]


# In[ ]:


sn.histplot(data = crim_boxcox, bins = 200, kde = True)


# In[ ]:


pd.crosstab(df['verified'], df['protected'])


# In[ ]:


pd.crosstab(df['default_profile'], df['protected'])


# In[ ]:


pd.crosstab(df['default_profile'], df['protected'])


# In[ ]:


pd.crosstab(df['default_profile'], df['default_profile_image'])


# In[ ]:


pd.crosstab(df['class'], df['verified'])


# In[ ]:


pd.crosstab(df['class'], df['protected'], margins = True)


# In[ ]:


pd.crosstab(df['protected'], df['verified'], margins = True)


# In[ ]:


pd.crosstab(df['verified'], df['class'], margins = True)


# In[ ]:


plt.clf()


# In[ ]:


plt.clf()
cross = pd.crosstab(index = [df['verified'], df['protected'], df['default_profile'], df['default_profile_image']], columns = df['class'])
plt.subplots(figsize=(10,10))
plt.tick_params(labelsize = 10)
sns.heatmap(cross, cmap = 'YlOrBr', cbar_kws = {'shrink': 0.8})
cross


# In[ ]:


df_bar = df[['verified', 'protected', 'class', 'default_profile', 'default_profile_image']]

fig_1 = sns.countplot(x = 'protected', data = df_bar, hue = 'class')
fig_2 = sns.countplot(x = 'default_profile', data = df_bar)
plt.show()


# In[ ]:


plt.close()


# In[ ]:


gc.collect()


# In[ ]:


df_p


# In[ ]:


df_pairplot = df[['statuses_count', 'followers_count', 'friends_count', 'favourites_count', 'listed_count', 'class']]


# In[ ]:


df_pairplot['statuses_count'] = np.log(df_pairplot['statuses_count']+1)
df_pairplot['followers_count'] = np.log(df_pairplot['followers_count']+1)
df_pairplot['friends_count'] = np.log(df_pairplot['friends_count']+1)
df_pairplot['favourites_count'] = np.log(df_pairplot['favourites_count']+1)
df_pairplot['listed_count'] = np.log(df_pairplot['listed_count']+1)


# In[ ]:


sns.pairplot(df_pairplot)


# In[ ]:


sns.pairplot(df_pairplot)
#plt.close()


# In[ ]:


plt.close()


# In[ ]:


sns.pairplot(df_pairplot, hue = 'class')


# In[ ]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(np.log(df['followers_count']+1), np.log(df['listed_count']+1), np.log(df['favourites_count']+1), c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


# In[ ]:


fig = px.scatter_3d(df, x=np.log(df['statuses_count']+1), y=np.log(df['followers_count']+1), z=np.log(df['listed_count']+1),color=df['class'],labels= True)
fig.show()


# In[ ]:


fig_5 = sm.qqplot(np.log(df['favourites_count']+1), line = '45')
fig_4 = sm.qqplot(np.log(df['listed_count']+1), line = '45')
fig_3 = sm.qqplot(np.log(df['followers_count']+1), line = '45')
fig_2 = sm.qqplot(np.log(df['statuses_count']+1), line = '45')
fig_1 = sm.qqplot(np.log(df['friends_count']+1), line = '45')
plt.show()


# In[ ]:


plt.scatter(np.log(df['followers_count']+1), np.log(df['friends_count']+1))

