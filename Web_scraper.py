#!/usr/bin/env python
# coding: utf-8

# In[9]:


# The Building Blocks
year = '2021'
url_link = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

# Combining the URL + year strings together
url = url_link.format(year)
url


# In[10]:


url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"


# In[11]:


import pandas as pd


# In[12]:


df = pd.read_html(url,header=0)
df


# In[13]:


len(df)


# In[ ]:





# In[5]:


df[0]


# In[19]:


df2021 = df[0]


# In[20]:


df2021[df2021.Age == 'Age']


# In[22]:


len(df2021[df2021.Age == 'Age'])


# In[26]:


import seaborn as sns


# In[ ]:




