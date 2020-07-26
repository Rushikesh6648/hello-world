#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv


# In[4]:


names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
 

r = requests.get('https://in.finance.yahoo.com/currencies')
soup = bs4.BeautifulSoup(r.text, "lxml")
 
counter = 40
for i in range(40, 404, 14):
   for listing in soup.find_all('tr', attrs={'data-reactid':i}):
      for name in listing.find_all('td', attrs={'data-reactid':i+3}):
         names.append(name.text)
      for price in listing.find_all('td', attrs={'data-reactid':i+4}):
         prices.append(price.text)
      for change in listing.find_all('td', attrs={'data-reactid':i+5}):
         changes.append(change.text)
      for percentChange in listing.find_all('td', attrs={'data-reactid':i+7}):
         percentChanges.append(percentChange.text)


# In[5]:


df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
df.to_csv('commodity.csv', index = False, encoding = 'utf-8' )
print("File Exoprted successfully")



# In[ ]:




