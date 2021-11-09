import requests as r
import bs4
from bs4 import BeautifulSoup
website = 'https://en.wikipedia.org/wiki/Basketball_statistics'
scraper = r.get(website)
soup = BeautifulSoup(scraper.text, 'html.parser')


# print(soup.find("span",{"class":"toctext"}).text)
#links
# title_list = soup.find_all(href=True)
# for i in title_list:
#     print(i.text)
#bold titles
title_list = soup.find_all('p')
for i in title_list:
    print(i.text)

