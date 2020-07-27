#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv


# In[7]:


prices=[]
names=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]


# In[8]:


CryptoCurrenciesUrl = ""
r = requests.get('https://in.finance.yahoo.com/world-indices')
soup = bs4.BeautifulSoup(r.text, "lxml")


# In[9]:


counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
         for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for change in srow.find_all('td', attrs={'class':'data-col3'}):
            changes.append(change.text)
         for percentChange in srow.find_all('td', attrs={'class':'data-col4'}):
            percentChanges.append(percentChange.text)


# In[10]:


df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
df.to_csv('commodity.csv', index = False, encoding = 'utf-8' )
print("File Exoprted successfully")



# In[ ]:




