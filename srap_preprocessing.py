import time
from pathlib import Path
import json


def try_post_date(article):
    try:
        post_date = article.find('span', {'class': 'txt_list_2'}).text  
    except:
        post_date = article.find('span', class_ = 'txt_list_important').text      
    return post_date   
from pathlib import Path
import json
     
    
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
       
    

def count_time(start, stop):
    duration = (stop - start)
    return round(duration, 2)

