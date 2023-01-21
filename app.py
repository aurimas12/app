from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from srap_preprocessing import upload_time, count_time, try_salary, try_applicants, try_post_date, stopwatch_time, count_posts
import time
from models import Post
import pandas as pd
from utils.file import create_csv, read_csv, create_json

class Crawler:
    def __init__(self, url):
        self.url = url
        self.csv_file = 'data.csv'
        self.json_file = 'data.json'
        self.posts = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


    def download_url(self):
        response = requests.get(self.url, headers=self.headers)  # timeout=1
        return response.headers
        

    def download_content(self, pages_index):
        print('total pages:', pages_index) 
        for page in tqdm(range(1, pages_index+1), ncols=100, colour="green", desc='Pages scraping progress'):
            full_source = requests.get(f'{self.url}{page}', headers=self.headers)
            full_soup = BeautifulSoup(full_source.content, 'lxml')
            articles = full_soup.find_all('article')
            for article in tqdm(articles, ncols=100, colour="yellow", desc='Posts scraping progress', leave=False):
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
                post_soup = BeautifulSoup(post_source.content, 'lxml')
                description_full = post_soup.find_all('section', itemprop='description')[0].get_text()
                applicants_value = try_applicants(post_soup)

                post = Post(post_id,post_url,img_url,position,company,city,salary,post_date,upload_post,description_full,applicants_value)
               
                self.posts.append(post.data_dict())   
        return self.posts
    

    def get_last_page_index(self):
        page_index = 1
        with requests.Session() as rs:
            while True:
                req = rs.get(f'{self.url}{page_index}')
                soup = BeautifulSoup(req.content, 'lxml')
                if soup.select_one('[rel=next]') is None:
                    break
                page_index += 1         
        return page_index

    
    def create_df(self):
        data_csv = {
            'website': "www.cvbankas.lt",
            'extract_time': self.count_time,
            'total_posts': self.count_posts,
            'posts': [self.posts],
            'created_date': self.time_now
        }
        df = pd.DataFrame(data_csv, columns=['website', 'extract_time', 'total_posts', 'posts', 'created_date'])
        return df


    def crawl(self):
        pages_index = self.get_last_page_index()
        page_content = self.download_content(pages_index)
        return page_content
    
      
    def run(self):
        start_time = time.perf_counter()
        self.time_now = time.strftime("%Y-%m-%d %H:%M:%S")
        print(self.time_now)
        self.count_posts = count_posts()
        print('total posts:', self.count_posts)
        self.crawl()
        stop_time = time.perf_counter()
        self.count_time = count_time(start_time, stop_time)
        # print(create_json(self.posts, self.json_file))
        print(create_csv(self.csv_file, self.create_df()))
        print(read_csv(self.csv_file))
        print(len(self.posts))
        print('web information extraction time', stopwatch_time(start_time, stop_time))


if __name__ == '__main__':
    Crawler(url='https://www.cvbankas.lt?page=').run()
