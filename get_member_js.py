#!/usr/bin/env python
# coding: utf-8

# In[3]:


#get_ipython().system('pip3 install beautifulsoup4')
#get_ipython().system('pip3 install lxml')
#get_ipython().system('pip3 install html5lib')


# In[4]:


import bs4
import json
import pandas as pd


# In[5]:


# exampleFile = open('js/members.txt')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html5lib')
# # print(exampleSoup)
# elems = exampleSoup.select('.user-information')
# print(type(elems))
# print(len(elems))
# # print(elems[0])
# # print(elems[0].getText())
#
# members = []
# for i, elem in enumerate(elems):
#     # print(i, elem)
#     if i >= 2:
#         href = elem.select('a')
#         # print(href)
#         login = href[0]['href'][-7:]+'@'
#         name = href[0].string
#         member = {'phone': login, 'name': name}
#         members.append(member)

# In[ ]:

persons = pd.read_excel('js/名单.xlsx')
print(persons.shape)
print(persons)

members = []

for idx, person in persons.iterrows():
    name = person['Name']
    login = person['Login']
    member = {'phone': login, 'name': name}
    members.append(member)

fout = open('js/member.js', 'w')

fout.write('var member=')

fout.write(json.dumps(members, indent=4))

fout.close()
