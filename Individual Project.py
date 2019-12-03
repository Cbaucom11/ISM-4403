#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df['Cars Sold'].mean()


# In[4]:


df['Cars Sold'].max()


# In[5]:


df['Cars Sold'].min()


# In[6]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[7]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


df['Years Experience'].mean()


# In[9]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[10]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[11]:


df['Hours Worked'].sum()


# In[12]:


df['Hours Worked'].mean()


# In[ ]:




