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

posts_list = []
for article in articles:
    post_id = article.find('div', {'class': 'jobadlist_ad_anchor'}).get("id")[6:]
    post_url = article.find("a", {"class": "list_a can_visited list_a_has_logo"}).attrs['href'] 
    img_url = article.find('img').get('src')
    position = article.find('h3').text
    company = article.find('span', {'class': 'dib mt5'}).text
    city = article.find('span', {'class': 'list_city'}).text

    try:
        salary = article.find('span', class_ = 'salary_amount').text
        salary_split = salary.split('-')
        salary_int =list(map(int, salary_split))
    except Exception:
        salary = " "
        
        
    try:
        post_date = article.find('span', {'class': 'txt_list_2'}).text
    except:
        post_date = article.find('span', class_ = 'txt_list_important').text      
            
    
                                    
    upload_post = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(upload_time(post_date)))


    post_source = requests.get(post_url)
    post_soup = BeautifulSoup(post_source.text, 'lxml')
        
    try:
        applicants_full = post_soup.find_all('div', class_='jobad_stat')[1].text
        applicants_value = applicants_full.split()[0]
    except:
        applicants_value = "0"

    post_descript_full = post_soup.find_all('div', {'class': 'jobad_txt'})
    post_descript = post_descript_full[0].text, post_descript_full[1].text

    # post_descript_full[1].text
    # post_descript_full[2].text
    # post_descript_full[3].text
    # post_descript_full[4].text 
    # post_descript_full[5].text


    post_data = {
        "post_descrip": post_descript,
        "post_id": post_id,
        "applicants": applicants_value,
        "post_url": post_url, 
        "img_url": img_url,
        "position": position, 
        "company": company, 
        "salary": salary,
        "city": city,
        "upload_post": upload_post,
        "time_public": post_date
            }
    
    posts_list.append(post_data)
    
print(posts_list)
print('Post scraping done.')

# for i in range(len(posts_list)):
#     print()
#     print(i, posts_list[i])


stop_time = time.perf_counter()   


# with open("cv_bankas_scrap.json", "a") as file:
#     json.dump(post, file, indent=2)
#     print(f'Informacija irasyta cv_bankas_scrap.json faile')


print(f'web information extraction time',count_time(start_time, stop_time))
