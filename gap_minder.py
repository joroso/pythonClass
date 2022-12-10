#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('data/gapminder.tsv.txt', sep='\t')


# In[5]:


df.head() # Returns first five 


# In[6]:


type(df)


# In[7]:


df.shape # Returns a tuple


# In[8]:


df.columns


# In[11]:


df.dtypes


# In[12]:


df.info()


# In[13]:


# Subsetting columns by name
country_df = df['country']


# In[14]:


country_df.head()


# In[17]:


country_df.tail()


# In[20]:


# You can use dot notation to call the column name attribute
country_df_dot = df.country
country_df_dot.head()


# In[22]:


subset = df[['country', 'continent', 'year']]
subset.head()


# In[23]:


subset.tail()


# In[27]:


# Subset columns by index position
#subset = df[[2]]


# In[28]:


df.tail(n=1) # OR df.tail(1)


# In[29]:


# Subsetting multiple rows
df.loc[[0, 99, 999]]


# In[30]:


subset_new = df.loc[[0, 99, 999]]


# In[33]:


subset_new.head()


# In[34]:


df.head(n=10)


# In[35]:


# For each year in our data, what was our average life expectancy? What about population and GDP?
# Wahat if we stratify by continent?
# How many countries are listed in each continent?


# In[37]:


# Grouped by means
df.groupby('year')['lifeExp'].mean()


# In[38]:


grouped_year_df = df.groupby('year')


# In[39]:


grouped_year_df


# In[40]:


grouped_year_df_lifeExp = grouped_year_df['lifeExp']


# In[41]:


grouped_year_df_lifeExp


# In[43]:


mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
mean_lifeExp_by_year


# In[45]:


df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()


# In[46]:


# Frequency counts
df.groupby('continent')['country'].nunique()


# In[49]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.plot()


# In[50]:


import seaborn as sns
anscombe = sns.load_dataset("anscombe")
anscombe


# In[52]:


import matplotlib.pyplot as plt
dataset_1 = anscombe[anscombe['dataset'] =='I']


# In[53]:


plt.plot(dataset_1['x'], dataset_1['y'])


# In[54]:


plt.plot(dataset_1['x'], dataset_1['y'], '0')


# In[56]:





# In[ ]:




