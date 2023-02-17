from pathlib import Path
import json
import pandas as pd


def create_json(posts_list, json_file):
    path = Path(f"data/{json_file}")
    if path.is_file():
        with open(path, "a") as file:
            json.dump(posts_list, file, indent=2)
            return f'The data is added to the <{json_file}> file'
    else:
        with open(path, "w") as file:
            json.dump(posts_list, file, indent=2)
            return f'created <{json_file}> file and data written to it'
        
              
def create_csv(csv_file, df):
    file_path = Path(f'data/{csv_file}')
    if file_path.exists():
        df.to_csv(file_path, index=False, mode="a", header=False)    
        return f'The data is added to the <{csv_file}> file.'
    else:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(file_path, index=False, mode="a", header=True)
        return f'created <{csv_file}> file and data written to it'


def read_csv(csv_file):
    file_path = Path(f'data/{csv_file}')
    read_df = pd.read_csv(file_path)
    return read_df 


def create_companies_df(read_df):
    read_companies_df = pd.read_csv('data/companys.csv')

    companys_lists = []
    new_companies_count = 0 
    for line in range(len(read_df)):
        line_posts=eval(read_df['posts'][line])
        for post in range(len(line_posts)):
            if line_posts[post]['company'] not in [i['company'] for i in companys_lists]:
                companys_lists.append({'company': line_posts[post]['company'], 'img_url': line_posts[post]['img_url']})

    for row in companys_lists:
        if not (read_companies_df['company'] == row['company']).any():
            new_companies_count += 1
            read_companies_df = pd.concat([read_companies_df, pd.DataFrame(row, index=[0])], ignore_index=True)

    read_companies_df.to_csv('data/companys.csv', index=False, mode="w", header=True) 
    return new_companies_count
