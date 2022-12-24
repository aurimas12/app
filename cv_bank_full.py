from bs4 import BeautifulSoup
import requests
import json
import time
from time import gmtime
from time import strftime
from srap_preprocessing import upload_time, count_time, try_salary, try_applicants, try_post_date, create_json,count_pages, count_posts
import pandas as pd
from pathlib import Path 


start_time = time.perf_counter() 
time_now = time.strftime("%Y-%m-%d %H:%M:%S")

count_all_posts = count_posts()
count_all_pages = count_pages()
print(count_all_pages)


posts_list = []
for page in range(1, count_all_pages+1):
    full_source = requests.get('https://www.cvbankas.lt/?page={page}')
    full_soup = BeautifulSoup(full_source.text, 'lxml')
    articles = full_soup.find_all('article')
    print (f"https://www.cvbankas.lt/?page={page}")
    
   
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
    
     
stop_time_lap1 = time.perf_counter() 
    
data_csv = {
        'website': ["www.cvbankas.lt"],
        'extract_time': [count_time(start_time, stop_time_lap1)],
        'total_posts': [count_all_posts],
        'posts': [posts_list],
        'created_date': [time_now]
        }
   
    
df = pd.DataFrame(data_csv, columns=['website', 'extract_time', 'total_posts', 'posts', 'created_date'])
# print(df)
filepath = Path('data/data.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
csv_data = df.to_csv('data/data.csv', index=False, mode="a", header=False) # index=False, header=False, mode="a")     


print('data scraping done.')

# print(create_json(posts_list))

stop_time_lap2 = time.perf_counter() 

stopwatch_time = count_time(start_time, stop_time_lap2)
stopwatch_strf = strftime("%Hh:%Mm:%Ss", gmtime(stopwatch_time))
print(f'web info extraction time: {stopwatch_strf}')

new_df = pd.read_csv('data/data.csv')
print(new_df)