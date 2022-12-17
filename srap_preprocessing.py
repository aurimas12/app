import time
from pathlib import Path
import json


def try_post_date(article):
    try:
        post_date = article.find('span', {'class': 'txt_list_2'}).text  
    except:
        post_date = article.find('span', class_ = 'txt_list_important').text      
    return post_date   

    
def upload_time(post_date):
     
    current_time = round(time.time())
    post_date_split = post_date.split()
    data_number = post_date_split[1]
    current_time = round(time.time())
    time_values = ['d.', 'val.', 'min.']

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
        return current_time
 
 
def try_applicants(post_soup):   
    try:
        applicants_full = post_soup.find_all('div', class_='jobad_stat')[1].text
        applicants_value = applicants_full.split()[0]
    except:
        applicants_value = "0"
    return applicants_value  


def try_salary(article):
    try:
        salary = article.find('span', class_ = 'salary_amount').text
        salary_split = salary.split('-')
        salary =list(map(int, salary_split))
    except Exception:
        salary = [0]
    return salary


def create_json(posts_list):
    json_file = "data.json"
    path = Path(json_file)
    
    if path.is_file():
        with open("data.json", "a") as file:
            json.dump(posts_list, file, indent=2)
            return f'The information is added to the <{json_file}> file'
    else:
        with open("data.json", "w") as file:
            json.dump(posts_list, file, indent=2)
            return f'created <{json_file}> file and Information written to it'


def count_time(start, stop):
    duration = (stop - start)
    return round(duration, 2)

