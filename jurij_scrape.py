from bs4 import BeautifulSoup
import requests
import json
import time
from srap_preprocessing import upload_time, count_time, try_salary, try_applicants, try_post_date, create_json


start_time = time.perf_counter() 
                         
source = requests.get('https://www.cvbankas.lt/?location=606&padalinys%5B%5D=76&keyw=python').text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')
print(f"amount of post:", len(articles)) 


posts_list = []
for article in articles:
    post_id = article.find('div', {'class': 'jobadlist_ad_anchor'}).get("id")[6:]
    post_url = article.find("a", {"class": "list_a can_visited list_a_has_logo"}).attrs['href'] 
    img_url = article.find('img').get('src')
    position = article.find('h3').text
    company = article.find('span', {'class': 'dib mt5'}).text
    city = article.find('span', {'class': 'list_city'}).text
    salary = try_salary(article)
    post_date = try_post_date(article)                           
    upload_post = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(upload_time(post_date)))


    post_source = requests.get(post_url)
    post_soup = BeautifulSoup(post_source.text, 'lxml')
    post_description_full= post_soup.find_all('section',itemprop='description')[0].get_text()   
    applicants_value = try_applicants(post_soup)

    post_data = {
        "post_descrip": post_description_full,
        "post_id": post_id,
        "applicants": applicants_value,
        "company": company, 
        "position": position,
        "post_url": post_url, 
        "img_url": img_url,
        "salary": salary,
        "city": city,
        "upload_post": upload_post,
        "time_public": post_date
            }
    
    posts_list.append(post_data)
    
# print(posts_list)
print('Post scraping done.')

for i in range(len(posts_list)):
    print()
    print(i, posts_list[i])


stop_time = time.perf_counter()   

# print(create_json(posts_list))

print(f'web information extraction time',count_time(start_time, stop_time))
