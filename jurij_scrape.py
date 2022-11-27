from bs4 import BeautifulSoup
import requests
import json
import time
from srap_preprocessing import upload_time, count_time


start_time = time.perf_counter() 
                         
source = requests.get('https://www.cvbankas.lt/?location=606&padalinys%5B%5D=76&keyw=python').text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')
print(f"amount of post:", len(articles)) 


article = articles[25]
post_id = article.find('div', {'class': 'jobadlist_ad_anchor'}).get("id")[6:]
post_url = article.find("a", {"class": "list_a can_visited list_a_has_logo"}).attrs['href'] 
img_url = article.find('img').get('src')
position = article.find('h3').text
company = article.find('span', {'class': 'dib mt5'}).text
post_date = article.find('span', {'class': 'txt_list_2'}).text
salary = article.find('span', {'class': 'salary_amount'}).text
city = article.find('span', {'class': 'list_city'}).text
salary_arr = list([salary])

                                  
upload_post = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(upload_time()))


post = {
        "post_id": post_id,
        "post_url": post_url, 
        "img_url": img_url,
        "position": position, 
        "company": company, 
        "salary": salary_arr,
        "city": city,
         "upload_post": upload_post,
        "time_public": post_date
        }
# print(post)
post_arr = []
for  item, val in post.items():
        post_arr.extend([item, val])

print(post_arr)

print('post scraping done.')


stop_time = time.perf_counter()   


# with open("cv_bankas_scrap.json", "a") as file:
#     json.dump(post, file, indent=2)
#     print(f'Informacija irasyta .json faile')


print(f'web information extraction time',count_time())
