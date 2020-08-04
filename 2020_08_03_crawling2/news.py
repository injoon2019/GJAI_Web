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

search_input = input()
for i in range(1, 102, 10):
    base_url = f'https://search.naver.com/search.naver?&where=news&query={search_input}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=31&start='
    #base_url = f'https://search.naver.com/search.naver?&where=news&query={search_input}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=48&'
    #start_num 은 10씩 올라감(페이지)
    start_num = i
    end_url = '&refresh_start=0'

    URL = base_url + str(start_num)+end_url
    print(URL)
    response = requests.get(URL)
    #BeautifulSoup으로 파싱, soup객체 반환
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_objects.append(soup)

#실습: 반복문으로 바꾸기
for soup in soup_objects:
    news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li')

    for news in news_section:
        a_tag = news.select_one('dl > dt > a')

        news_title = a_tag['title']
        news_link = a_tag['href']

        news_data={
            'title':news_title,
            'link':news_link
        }

        with open(f"{search_input}news.csv", "a+", newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(news_data)
