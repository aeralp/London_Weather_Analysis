#!/usr/bin/env python
# coding: utf-8

# # London Weather - Time Series Analysis
# 

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv("london_weather.csv")


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.info()


# In[7]:


data.date =pd.to_datetime(data.date,format = "%Y%m%d")


# In[8]:


data.date.head()


# In[9]:


data.head()


# In[10]:


data.tail()


# In[11]:


data.set_index(keys="date", inplace = True)


# In[12]:


data_yearly = data.resample("AS").mean()


# In[13]:


data.head()


# In[14]:


data_yearly.head()


# In[15]:


data_yearly.global_radiation.tail()


# In[16]:


data_yearly.mean_temp.plot()


# In[17]:


data_yearly.min_temp.plot()


# In[18]:


data_yearly.max_temp.plot()


# In[19]:


yearly_size = data.resample("AS").size()


# In[20]:


yearly_size


# In[21]:


#there is not any suspect info given 
#data seems clear


# In[22]:


monthly =data.mean_temp.resample("M",kind = "period").mean()


# In[23]:


monthly.head()


# In[24]:


monthly.index.month


# In[25]:


#let's take a quick trend on April


# In[26]:


monthly.index.month == 4


# In[27]:


monthly_april = monthly[monthly.index.month == 4]


# In[28]:


monthly_april.head()


# In[35]:


monthly_april.plot(kind ="bar",title = "April",legend = True,color = "g",alpha =0.8)


# In[ ]:




