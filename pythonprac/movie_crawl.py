import requests
from bs4 import BeautifulSoup #beautifulsoup 패키지 설치해 활용

from pymongo import MongoClient #db는 pymongo
client = MongoClient('localhost', 27017)
db = client.dbjann #dbjann 저장

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# URL 읽어서 HTML 받아오기
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20220127',headers=headers)
#20220127네이버 영화 순위 받아오기

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr') # select 이용해 trs 불러오기

for tr in trs: # movies (tr들) 의 반복문 돌리기
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:         # a_tag가 비워있지 않으면 아래의 값 출력
        rank = tr.select_one('td:nth-child(1) > img')['alt'] #a_tag아닌 tr 선택자 - 순위: img 태그 alt 속성값
        title = a_tag.text #a_tag 제목- text만 출력
        star = tr.select_one('td.point').text #a_tag아닌 tr 선택자 - 평점 - td 태그 사이 text만 출력
        doc = { #doc {} 딕셔너리 형태로 저장
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc) #db - movies 에 딕셔너리 형태로 저장
        print(rank, title, star) #순위, 제목, 평점 출력
