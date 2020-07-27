#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


from bs4 import BeautifulSoup
import requests


# In[18]:


names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]


# In[19]:


for i in range(0,10):
  CryptoCurrenciesUrl = "https://in.finance.yahoo.com/cryptocurrencies?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=50"
  r = requests.get(CryptoCurrenciesUrl)
  data = r.text
  soup = BeautifulSoup(data, "lxml")



# In[20]:


for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
    for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
    for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
    for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
    for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
    for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
    for totalVolume in listing.find_all('td', attrs={'aria-label':'Total volume all currencies (24 hrs)'}):
      totalVolumes.append(totalVolume.text)
    for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating supply'}):
      circulatingSupplys.append(circulatingSupply.text)


# In[ ]:
df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
df.to_csv('commodity.csv', index = False, encoding = 'utf-8' )
print("File Exoprted successfully")




