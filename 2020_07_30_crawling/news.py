import requests
from bs4 import BeautifulSoup

# response = requests.get("https://naver.com")
# print(response.text)

# pipenv 설치 -> pipenv로 install requests bs4 하기 -> 파이썬 파일 만들기
# requests로 https://www.naver.com에 요청보내기 -> response.txt 출력하기 

base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=48&'
#start_num 은 10씩 올라감(페이지)
start_num = 1
end_url = '&refresh_start=0'
URL = base_url + str(start_num)+end_url

response = requests.get(URL)
#BeautifulSoup으로 파싱, soup객체 반환
soup = BeautifulSoup(response.text, 'html.parser')

news_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws >  ul[class=type01] >li')

for news in news_section:
    #attribute는 []로 가져온다
    print(news.select_one('dl > dt > a')['title'])
    print(news.select_one('dl > dt > a')['href'], '\n')