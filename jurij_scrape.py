from bs4 import BeautifulSoup
import requests
import json
import time


def count_time():
        duration = (stop_time-start_time)
        return round(duration, 2)


start_time = time.time() 
                         
source = requests.get('https://www.cvbankas.lt/?location=606&padalinys%5B%5D=76&keyw=python').text
soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')
print(f"amount of post:", len(articles)) 


article = articles[20]
post_url = article.find("a", {"class": "list_a can_visited list_a_has_logo"}).attrs['href'] 
img_url = article.find('img').get('src')
position = article.find('h3').text
company = article.find('span', {'class': 'dib mt5'}).text
date = article.find('span', {'class': 'txt_list_2'}).text
salary = article.find('span', {'class': 'salary_amount'}).text
city = article.find('span', {'class': 'list_city'}).text

post = {
        "post_url": post_url, 
        "img_url": img_url,
        "position": position, 
        "company": company, 
        "salary": salary,
        "city": city,
        "date": date
        }
print(post)
stop_time = time.time()  

with open("cv_bankas_scrap.json", "a") as file:
    json.dump(post, file, indent=2)
    print(f'Informacija irasyta .json faile')


print(f'web information extraction time',count_time())
