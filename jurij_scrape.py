from bs4 import BeautifulSoup
import requests
import json
import time


def count_time():
        duration = (stop_time-start_time)
        return round(duration, 2)


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


current_time = round(time.time())
post_date_split = post_date.split()
data_number = post_date_split[1]
current_time = round(time.time())
time_values = ['val.', 'min.', 'd.']

def upload_time():
        for x in post_date_split:
                if x in time_values:
                        if x == "d.":
                                temp_days = int(data_number) * 86400
                                post_upload = current_time - temp_days
                                return post_upload
                        
                        if x == "val.":
                                temp_hour = int(data_number) * 3600
                                post_upload = current_time - temp_hour
                                return post_upload
                        
                        if x == "min.":
                                temp_min = int(data_number) * 60
                                post_upload = current_time - temp_min
                                return post_upload
                        else:
                                return  # neveikia !!!!! palikau 

                                  
up = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(upload_time()))


post = {
        "post_id": post_id,
        "post_url": post_url, 
        "img_url": img_url,
        "position": position, 
        "company": company, 
        "salary": salary,
        "city": city,
         "upload_post": up,
        "time_public": post_date
        }
print(post)

stop_time = time.perf_counter()   


with open("cv_bankas_scrap.json", "a") as file:
    json.dump(post, file, indent=2)
    print(f'Informacija irasyta .json faile')


print(f'web information extraction time',count_time())
