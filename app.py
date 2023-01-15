from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from srap_preprocessing import upload_time, count_time, try_salary, try_applicants, try_post_date, count_pages, count_posts
import time

class Crawler:
    def __init__(self, url):
        self.url = url
        # self.header = HEADERS
        self.pages = []
        self. data = []
        self.posts = []


    def download_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        # response = requests.get(url.strip(), headers=headers, timeout=1)
        response = requests.get(self.url, headers=headers, timeout=1)
        # source = requests.get('https://www.cvbankas.lt/?page={page}')
        # return response
        print(response)


    def download_content(self, pages_index): 
        # last_page_index = x.get_last_page_index()
        print(f'page index {pages_index}')
        for page in tqdm(range(1, 2), ncols=100, colour="green", desc='Pages scraping progress'):
            full_source = requests.get(f'{self.url}{page}')
            full_soup = BeautifulSoup(full_source.text, 'lxml')
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
                post_soup = BeautifulSoup(post_source.text, 'lxml')
                post_description_full = post_soup.find_all('section', itemprop='description')[0].get_text()
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
                
                self.posts.append(post_data)           
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
        return page_index + 1


    def crawl(self):
        pages_index = self.get_last_page_index()
        page_content = self.download_content(pages_index)
        return page_content
    
    
    def run(self):
        self.crawl()
        

if __name__ == '__main__':
    Crawler(url = 'https://www.cvbankas.lt?page=').run()
    pass
