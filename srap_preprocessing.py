import time
from pathlib import Path
import json
     
     
def upload_time(post_date):
     
    current_time = round(time.time())
    post_date_split = post_date.split()
    data_number = post_date_split[1]
    data_value = post_date_split[2]
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
        print(f'value : {data_value} not in time_values')
    
    
def create_json(post):
    json_file = "data.json"
    path = Path(json_file)
    
    if path.is_file():
        with open("data.json", "a") as file:
            json.dump(post, file, indent=2)
            return f'The information is added to the <{json_file}> file'
    else:
        with open("data.json", "w") as file:
            json.dump(post, file, indent=2)
            return f'created <{json_file}> file and Information written to it'
        
        
def count_time(start, stop):
    duration = (stop - start)
    return round(duration, 2)

