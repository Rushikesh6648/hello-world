#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import requests 
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


prices=[]
names=[]
changes=[]
percentChanges=[]
marketCaps=[]
marketTimes=[]
totalVolumes=[]
openInterests=[]


# In[3]:



r= requests.get('https://in.finance.yahoo.com/commodities')

soup = BeautifulSoup(r.text, "lxml")


# In[6]:


counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('th', attrs={'class':'data-col1'}):
            names.append(name.text)
         for price in srow.find_all('th', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for time in srow.find_all('th', attrs={'class':'data-col3'}):
            marketTimes.append(time.text)
         for change in srow.find_all('th', attrs={'class':'data-col4'}):
            changes.append(change.text)
         for percentChange in srow.find_all('th', attrs={'class':'data-col5'}):
            percentChanges.append(percentChange.text)
         for volume in srow.find_all('th', attrs={'class':'data-col6'}):
            totalVolumes.append(volume.text)
         for openInterest in srow.find_all('th', attrs={'class':'data-col7'}):
            openInterests.append(openInterest.text)


df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Time": marketTimes,'Open Interest': openInterests ,"Volume": totalVolumes})
df.to_csv('commodity.csv', index = False, encoding = 'utf-8' )
print("File Exoprted successfully")







