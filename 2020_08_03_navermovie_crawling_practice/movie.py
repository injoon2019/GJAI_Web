import requests
from bs4 import BeautifulSoup
import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# response = requests.get("https://naver.com")
# print(response.text)

# pipenv 설치 -> pipenv로 install requests bs4 하기 -> 파이썬 파일 만들기
# requests로 https://www.naver.com에 요청보내기 -> response.txt 출력하기 

soup_objects = []

base_url = f'https://movie.naver.com/movie/running/current.nhn'
URL = base_url
print(URL)
response = requests.get(URL)
#BeautifulSoup으로 파싱, soup객체 반환
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li')
for movie in movie_section:
     a_tag = movie.select_one('dl > dt > a')

     movie_title = a_tag.text
     movie_code_index = a_tag['href'].index("=")
     movie_code = a_tag['href'][movie_code_index+1:]

     movie_data={
         'title':movie_title,
         'code': movie_code
     }


     with open("movie.csv", "a+", newline='', encoding='utf-8') as csvfile:
         fieldnames = ['title', 'code']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         writer.writerow(movie_data)
