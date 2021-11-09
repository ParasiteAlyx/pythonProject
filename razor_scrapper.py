from typing import Type
import requests as r
import numpy as np
import bs4
import pandas as pd
from decimal import Decimal
from bs4 import BeautifulSoup
import matplotlib as plt

website = 'https://www.westcoastshaving.com/collections/top-10-razor-blades'
scraper = r.get(website)
soup = BeautifulSoup(scraper.text, 'html.parser')


# print(soup.find("span",{"class":"toctext"}).text)
#links
# title_list = soup.find_all(href=True)
# for i in title_list:
#     print(i.text)
#bold titles
money_list = soup.find_all('span',{'class':'money'})
title_list = soup.find_all(href=True)

prices = []
titles = []
for i in money_list:
     prices.append(i.text)
df = pd.DataFrame(prices)
# df = df.rename(columns = {0:"Prices of Razors"},inplace=True)
# df
df['real_dollars'] = df[0].astype('string')
df['real_dollars'] = [x.strip(' $ ') for x in df['real_dollars']]
df['real_dollars'] = [x.strip(' ') for x in df['real_dollars']]
df['real_dollars'] = [x.strip('"') for x in df['real_dollars']]

# df['real_dollars'] = df['real_dollars'].astype('float')
# df['razor_blade_average_cost'] = np.mean(df['real_dollars'])
# print(df)
df.groupby('real_dollars').count()
