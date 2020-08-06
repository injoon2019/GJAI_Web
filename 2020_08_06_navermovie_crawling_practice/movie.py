import requests
from bs4 import BeautifulSoup
import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') 

soup_objects = []

base_url = f'https://movie.naver.com/movie/running/current.nhn'
URL = base_url
print(URL)
response = requests.get(URL)
#BeautifulSoup으로 파싱, soup객체 반환
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select('#content > .article > .obj_section > .lst_wrap > ul > li')
movie_data_list = []
for movie in movie_section:
     a_tag = movie.select_one('dl > dt > a')

     movie_title = a_tag.text
     movie_code = a_tag['href'].split("code=")[1]

     movie_data={
         'title':movie_title,
         'code': movie_code
     }
     
     movie_data_list.append(movie_data)


###code와 title은 가져왔다
#iframe 이란 것 때문에 가져오지 못하는 상황. 
#크롬 개발자도구에서 network가서 새로고침하고 원하는 부분가서 copy -> copy as cURL(bash) -> https://curl.trillworks.com/ -> convert
# 


# headers = {
#     'authority': 'movie.naver.com',
#     'cache-control': 'max-age=0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'none',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cookie': 'NNB=2ICNOMPGPQAF6; NRTK=ag#20s_gr#1_ma#-2_si#0_en#0_sp#0; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.2.90196555.1596087113; nx_ssl=2; page_uid=UyWwklp0J1ZsseJncaZssssssqZ-390187; csrf_token=af69cefe-5f27-456d-9f7e-eaeb2ccb20d6',
# }

# params = (
#     ('code', '189069'),
# )

# response = requests.get('https://movie.naver.com/movie/bi/mi/point.nhn', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://movie.naver.com/movie/bi/mi/point.nhn?code=189069', headers=headers)


headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=2ICNOMPGPQAF6; NRTK=ag#20s_gr#1_ma#-2_si#0_en#0_sp#0; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.2.90196555.1596087113; nx_ssl=2; page_uid=UyWwklp0J1ZsseJncaZssssssqZ-390187; csrf_token=094d6269-c1dd-4e94-b77a-fb8b2a08d713',
}




for movie_dict in movie_data_list:
    print("\n")
    print("\n")
    print(movie_dict['title'])

    
    params = (
        ('code', movie_dict['code']),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    review_section = soup.select('body > div > div > div.score_result > ul > li')
    score_and_review = []

    for i, review in enumerate(review_section):
        score = review.select_one('div.star_score > em').get_text()
        
        try:
            text = review.select_one(f'div.score_reple > p > span#_filtered_ment_{i}').text.strip()
      
        except:
            text = review.select_one(f'div.score_reple > p > span#_filtered_ment_{i} > span > a')['data-src']
        
        score_and_review.append((score, text))

    print(score_and_review)

