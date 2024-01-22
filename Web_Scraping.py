#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)


# In[7]:


table = soup.find_all('table')[1]


# In[8]:


print(table)


# In[14]:


world_titles = table.find_all('th')
print(world_titles)


# In[17]:


world_table_title = [title.text.strip() for title in world_titles]
print(world_table_title)


# In[18]:


import pandas as pd


# In[19]:


df = pd.DataFrame(columns = world_table_title)


# In[21]:


df


# In[24]:


column_data = table.find_all('tr')
print(column_data)


# In[29]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [ind_row.text.strip()for ind_row in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[30]:


df


# In[32]:


df.to_csv(r'/Users/virendpatil/Desktop/WebScraping/Companies.csv', index = False)


# In[ ]:




