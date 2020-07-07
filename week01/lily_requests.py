
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
movieList = []
count = 0
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    #print("tags: *****")
    #print(tags)
    
    film = set()
    for dtag in tags.find_all('div'):
        nameTag = dtag.find('span', attrs={'class':'name'})
        
        if nameTag != None:
            name = nameTag.text
            print(f'{name}')
            film.add(f'{name}')

        typeAndTimeTag = dtag.find('span', attrs={'hover-tag'})
        if typeAndTimeTag != None:
            typeAndTimeText = typeAndTimeTag.text
            if (typeAndTimeText == '类型:'):
                filmType = dtag.text.replace('\n', '').replace(' ','')
                print(f'{filmType}')
                film.add(f'{filmType}')
              
            if (typeAndTimeText == '上映时间:'):
                filmDate = dtag.text.replace('\n', '').replace(' ','')
                print(f'{filmDate}')
                film.add(f'{filmDate}')
    movieList.append(film)
    count = count +1       
    if count >= 10:
        break

import pandas as pd

movie = pd.DataFrame(data = movieList)

# windows需要使用gbk字符集
movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)
