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
# print(type(count_all_pages))
print(count_all_pages)


for page in range(1, count_all_pages):
    print(page)
    full_source = requests.get('https://www.cvbankas.lt/?page={page}')
    full_soup = BeautifulSoup(full_source.text, 'lxml')
    articles = full_soup.find_all('article')
    # x +=  len(all_posts)
    # print(f"amount of post:", len(articles))

    print (f"https://www.cvbankas.lt/?page={page}")
    
# articles = soup.find_all('article')
    # print(f"amount of post in search of python:", len(articles)) 

    # count_all_posts = count_posts()
# print(f'amount of posts', count_posts())
# print(f'number of pages', count_pages())


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
    
     
stop_time = time.perf_counter() 
    
data_csv = {
        'website': ["www.cvbankas.lt"],
        'extract_time': [count_time(start_time, stop_time)],
        'total_posts': [count_all_posts],
        'posts': [posts_list],
        'created_date': [time_now]
    }
   
    
df = pd.DataFrame(data_csv, columns=['website', 'extract_time', 'total_posts', 'posts', 'created_date'])
# Printing DataFrame
# print(df)
    # data = data.append({'website', 'extract_time', 'total_posts', 'posts', 'created_date' })
filepath = Path('data/data.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
csv_data = df.to_csv('data/data.csv', index=False, mode="a") #, header=False) # index=False, header=False, mode="a")     

# print(posts_list)


# for i in range(len(posts_list)):
#     print()
#     print(i, posts_list[i])

print('Post scraping done.')

# stop_time = time.perf_counter()   

# print(create_json(posts_list))
x = count_time(start_time, stop_time)
z = strftime("%Hh:%Mm:%Ss", gmtime(x))
print(f'web information extraction time', z)

new_df = pd.read_csv('data/data.csv')
print(new_df)