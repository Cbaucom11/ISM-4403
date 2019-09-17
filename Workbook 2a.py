#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob("C:\Users\Caden Baucom\weekly_call_data\weekdata_*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()

