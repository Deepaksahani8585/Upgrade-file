#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


# In[3]:


df=pd.read_csv("Test_data.csv")


# In[4]:


df.head(10)


# In[5]:


df.shape # to check row and columns


# In[6]:


df.tail(10)


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.isnull().sum()


# In[10]:


df=df.drop("previous_year_rating",axis=1)
# delete this column because this column has more null values.


# In[11]:


df=df.drop("education",axis=1)


# In[12]:


df.isnull().sum()


# In[14]:


sns.barplot(y=df["age"],x=df["gender"])


# In[55]:


sns.distplot(df["age"])


# In[16]:


plt.hist(df["age"])
plt.xlabel("age")
plt.ylabel("Frequency")
plt.title("Distribution of age")
plt.show()


# In[17]:


sns.countplot(x="age",data=df)


# In[18]:


sns.countplot(x="gender",data=df)


# In[28]:


sns.countplot(y="department",data=df)


# In[ ]:





# In[32]:


sns.countplot(x="KPIs_met >80%",data=df)


# In[51]:


sns.boxplot(x="gender",y="avg_training_score",data=df,hue="gender")


# In[53]:


sns.boxplot(y="age",x="department",data=df)


# In[ ]:




