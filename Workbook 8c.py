#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

Location = "datasets/gradedata2.csv"
df = pd.read_csv(Location)
df.head()

df.plot.scatter(x='hours', y='grade')


# In[ ]:




