#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests
import schedule
import time


# In[3]:


biggest_cities = []

biggest_cities.append('https://news.yandex.ru/Kaliningrad/index.rss')
biggest_cities.append('https://news.yandex.ru/Moscow_and_Moscow_Oblast/index.rss')
biggest_cities.append('https://news.yandex.ru/Krasnodar/index.rss')
biggest_cities.append('https://news.yandex.ru/Saint_Petersburg/index.rss')
biggest_cities.append('https://news.yandex.ru/Yekaterinburg/index.rss')
biggest_cities.append('https://news.yandex.ru/Rostov-na-Donu/index.rss')
biggest_cities.append('https://news.yandex.ru/Ufa/index.rss')
biggest_cities.append('https://news.yandex.ru/Kazan/index.rss')
biggest_cities.append('https://news.yandex.ru/Tyumen/index.rss')
biggest_cities.append('https://news.yandex.ru/Chelyabinsk/index.rss')
biggest_cities.append('https://news.yandex.ru/Nizhny_Novgorod/index.rss')


# In[9]:


def read_rss():
    for city_rss in biggest_cities:
        html_doc = requests.get(city_rss).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        data = []
        for item in soup.find_all('item'):
            try:
                data.append([item.title.text, item.link.text, item.description.text, item.pubdate.text, city_rss])
            except Exception as e:
                print(e)
        news_columns = ['title', 'link', 'text', 'date', 'city_rss']
        news = pd.DataFrame(data, columns = news_columns)
        print(len(news.index))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        news.to_csv('news.csv', mode='a+', index=False, header=False)


# In[15]:


schedule.every(2).hours.do(read_rss)

while True:
    schedule.run_pending()
    time.sleep(2*60*60)


# In[11]:


# read_rss()


# In[ ]:




