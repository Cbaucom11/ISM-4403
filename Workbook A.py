#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
Location = "C:\Users\Caden Baucom\datasets\gradedata.csv"
# add headers to imported data
df = pd.read_csv(Location)
df.head()

