#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
Location = "C:\Users\Caden Baucom\datasets\gradedata2.csv"
df = pd.read_csv(Location)
df.head()


# In[24]:


df = df.sort_values(by=['lname','age','grade'],
                    ascending=[True,True,True])
df.head()

