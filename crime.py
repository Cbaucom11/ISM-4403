#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "C:\Users\Caden Baucom\datasets\crime.xls"
# add headers to imported data
df = pd.read_excel(Location)
df.head()

