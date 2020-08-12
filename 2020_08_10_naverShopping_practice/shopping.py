import requests
from bs4 import BeautifulSoup
import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') 

soup_objects = []

URL = f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=rel&timestamp=&viewType=list'
print(URL)
response = requests.get(URL)
#BeautifulSoup으로 파싱, soup객체 반환
soup = BeautifulSoup(response.text, 'html.parser')
#shopping_section = soup.select('#__next > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul ')
#for shopping in shopping_section:
for i in range(1, 50):
    #item = soup.select(f'#__next > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child({i}) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a')
    #__next > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(5) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a
    a_tag = soup.find('#__next > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(5) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a'.format(i))
    print(a_tag.text, end="\n\n")

# for i in range(1, 50):
    print('#__next > div > div.container > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child({}) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a'.format(i))
