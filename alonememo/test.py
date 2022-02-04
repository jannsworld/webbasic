import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title : content > div.article > div.wide_info_area > div.mv_info > h3 > a
# img : content > div.article > div.wide_info_area > div.poster > a > img
title = soup.select_one('meta[property="og:title"]')['content']
img = soup.select_one('meta[property="og:image"]')['content']
description = soup.select_one('meta[property="og:description"]')['content']
print(title, img, description)