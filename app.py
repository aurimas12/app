from bs4 import BeautifulSoup
import requests


class Crawler:
    def __init__(self, url):
        self.url = url
        # self.header = HEADERS
        self.pages = []
        self. data = []


    def download_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        # response = requests.get(url.strip(), headers=headers, timeout=1)
        response = requests.get(self.url, headers=headers, timeout=1)
        source = requests.get('https://www.cvbankas.lt/?page={page}')
        # return response
        print(response)


    def download_content(self): 
        last_page_index = x.get_last_page_index()
        print(f'page number {last_page_index}')
        full_article = []
        amount_post = 0
        page_number = 1
        with requests.Session() as rs:
            while page_number != last_page_index:
                req = rs.get(f'https://www.cvbankas.lt/?page={page_number}')
                soup = BeautifulSoup(req.content, 'lxml')
                articles = soup.find_all('article')
                print('len-', len(articles))
                print('page number-',page_number)
                amount_post += len(articles)
                page_number += 1  
                full_article.extend(articles)
        return len(full_article)
    

    def get_last_page_index(self):
        page_index = 1
        with requests.Session() as rs:
            while True:
                req = rs.get(f'https://www.cvbankas.lt/?page={page_index}')
                soup = BeautifulSoup(req.content, 'lxml')
                if soup.select_one('[rel=next]') is None:
                    break
                page_index += 1        
        return page_index + 1


    def crawl(self, url):
        pass

    def run(self):
        pass


x = Crawler('https://www.cvbankas.lt/?page=')
# print(x.download_url())
# print(x.get_last_page_index())
print(x.download_content())

if __name__ == '__main__':
    # Crawler(url = https://www.cvbankas.lt).run()
    pass
