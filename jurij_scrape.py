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

salary_split = salary.rsplit('-')
salary_int =list(map(int, salary_split))
  
                                  
upload_post = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(upload_time(post_date)))

post_source = requests.get(post_url)
post_soup = BeautifulSoup(post_source.text, 'lxml')


job_h2 = post_soup.find_all('h2')
job_full = post_soup.find_all('div', {'class': 'jobad_txt'})

job_head_desc = job_h2[0].text
job_descrip = post_soup.find('div', {'class': 'jobad_txt'}).text
job_head_candid = job_h2[1].text
job_cand_full= job_full[1]
job_candidate = job_cand_full.text
job_head_requir = job_h2[2].text
job_reguir_ful = job_full[2]
job_requirement = job_reguir_ful.text
job_head_salary = job_h2[3].text
job_salary_full = job_full[3]
job_sal= job_salary_full.text
job_sal_format = (''.join([ch for ch in job_sal if ch not in [' ', '\t', '\n']]))

job_description = {
    "job_head_desc": job_head_desc,
    "job_descrip": job_descrip,
    "job_head_candid":job_head_candid,
    "job_candidate": job_candidate,
    "job_head_requirement": job_head_requir,
    "job_requirement": job_requirement,
    "job_head_salary": job_head_salary,
    "job_salary_format": job_sal_format,
    }   

post = {
    "job_description": job_description,
    "post_id": post_id,
    "post_url": post_url, 
    "img_url": img_url,
    "position": position, 
    "company": company, 
    "salary": salary_int,
    "city": city,
    "upload_post": upload_post,
    "time_public": post_date
        }

# print(post)
print('Post scraping done.')


stop_time = time.perf_counter()   


# with open("cv_bankas_scrap.json", "a") as file:
#     json.dump(post, file, indent=2)
#     print(f'Informacija irasyta cv_bankas_scrap.json faile')


print(f'web information extraction time',count_time(start_time, stop_time))
