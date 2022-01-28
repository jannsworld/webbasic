import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient #db는 pymongo
client = MongoClient('localhost', 27017)
db = client.dbjann #dbjann 저장

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220128&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
        #.text[0:2] : 0에서 2까지 텍스트만 출력 , .strip() 통해서 공백 제거
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    singer = tr.select_one('td.info > a.artist.ellipsis').text

    doc = {  # doc {} 딕셔너리 형태로 저장
        'rank': rank,
        'title': title,
        'singer': singer
    }
    db.musics.insert_one(doc)  # db - musics 에 딕셔너리 형태로 저장
    print(rank, title, singer)