#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
url=BeautifulSoup('https://www.worldometers.info/coronavirus/','html.parser')
start=requests.get(url)
s1=start.text
soup=BeautifulSoup(s1,'lxml')
tags=soup.table
tag=tags.find_all('tr')
list1=[]
for i in range(len(tag)):
    x=tag[i].get_text()
    list1.append(x)
del list1[1:7]
del list1[1:3]
list1=list1[:216]
final=[]
for j in list1:
    y=j.split('\n')[1:-1]
    final.append(y)
for k in range(len(final)):
    del final[k][-2:]
final[0]=['#',
  'Country,other',
  'TotalCases',
  'NewCases',
  'TotalDeaths',
  'NewDeaths',
  'TotalRecovered',
  'NewRecovered',
  'ActiveCases',
  'Serious,Critical',
  'TotalCases/1M pop',
  'Deaths/1M pop',
  'TotalTests',
  'Tests/1M pop',
  'Population']
#print(final[2])
print(final)
#print(len(final[0]))


# In[10]:


import csv
with open("out.csv", "w", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(final)


# In[11]:


import pandas as pd
x=pd.read_csv('out.csv')
x


# In[3]:


# print("f")


# In[ ]:





# In[ ]:





# In[ ]:





# In[74]:


from bs4 import BeautifulSoup
import requests
url=BeautifulSoup('http://www.nepalstock.com/indices','html.parser')
start=requests.get(url)
v1=start.text
soup=BeautifulSoup(v1,'lxml')
tags=soup.table
tag=tags.find_all('tr')
list1=[]
#print(len(tag))
for i in range(len(tag)):
    x=tag[i].get_text()
    list1.append(x)
list1=list1[1:]
final=[]
for i in list1:
    y=i.split('\n')[1:-1]
    final.append(y)
print(final)


# In[75]:


import csv
n = len(final)
with open('stock1.csv','a') as csvFile:
  writer = csv.writer(csvFile)
  for i in range(n):
    writer.writerow(final[i])
import pandas as pd
x=pd.read_csv('stock1.csv')
x


# In[37]:


x=[[2,6,8],[32,2,5,9,4],[56,8,4,32]]
for i in range(len(x)):
    del x[i][-2:]
x


# In[39]:


x=[[2,6,8],[32,2,5,9,4],[56,8,4,32]]
for i in range(len(x)):
    del x[i][-2:]
x


# In[57]:


x=[1,3,5,6]
list1=[]
for i in x:
    y=str(i)
    list1.append(y)
x=list1[2:]
x
list2="".join(x)
list2    


# In[69]:


x=['#',
  'Country,Other',
  'TotalCases',
  'NewCases',
  'TotalDeaths',
  'NewDeaths',
  'TotalRecovered',
  'NewRecovered',
  'ActiveCases',
  'Serious,Critical',
  'Tot\xa0Cases/1M pop',
  'Deaths/1M pop',
  'TotalTests',
  'Tests/',
  '1M pop',
  '',
  'Population']
y=x[13:16]
z="".join(y)
z


# In[72]:


x=['#',
  'Country,Other',
  'TotalCases',
  'NewCases',
  'TotalDeaths',
  'NewDeaths',
  'TotalRecovered',
  'NewRecovered',
  'ActiveCases',
  'Serious,Critical',
  'Tot\xa0Cases/1M pop',
  'Deaths/1M pop',
  'TotalTests',
  'Tests/1M pop',
  'Population']
print(len(x))


# In[68]:


x=[[1,43,6,7,4],[6,8,9,3],[3,8,9,34]]
x[0]=[6,6,6,6,6]
print(x)


# In[113]:


from bs4 import BeautifulSoup
import requests
url=BeautifulSoup('https://www.worldometers.info/coronavirus/','html.parser')
start=requests.get(url)
s1=start.text
soup=BeautifulSoup(s1,'lxml')
tags=soup.table
tag=tags.find_all('tr')
list1=[]
for i in range(len(tag)):
    x=tag[i].get_text()
    list1.append(x)
del list1[1:7]
del list1[1:3]
list1=list1[:216]
final=[]
for j in list1:
    y=j.split('\n')[1:-1]
    final.append(y)
for k in range(len(final)):
    del final[k][-2:]
    del final[k][7]
final[0]=['#',
  'Country,other',
  'TotalCases',
  'NewCases',
  'TotalDeaths',
  'NewDeaths',
  'TotalRecovered',
  'ActiveCases',
  'Serious,Critical',
  'TotalCases/1M pop',
  'Deaths/1M pop',
  'TotalTests',
  'Tests/1M pop',
  'Population']
print(final)
#print(final[2])
#print(len(final[0]))


# In[114]:


import csv
n = len(final)
with open('world.csv','a') as csvFile:
  writer = csv.writer(csvFile)
  for i in range(n):
    writer.writerow(final[i])


# In[116]:


x=["a","f",'',"s","r",'']
for i in range(len(x)):
    if '' in x:
    x.replace()


# In[ ]:




