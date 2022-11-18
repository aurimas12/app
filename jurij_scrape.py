from bs4 import BeautifulSoup
import requests
import json

# user_input = input("Iveskite paieskos zodi fraze: ")
# template = "https://www.cvbankas.lt/?location=&padalinys%5B%5D=&keyw={}"

# def get_url(keyword):
#     template = "https://www.cvbankas.lt/?location=&padalinys%5B%5D=&keyw={}"
#     url = template.format(keyword)
#     return url
                       
# url = get_url(user_input)                         
   
   
# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')
# articles = soup.find_all('article')
                          
source = requests.get('https://www.cvbankas.lt/?location=606&padalinys%5B%5D=76&keyw=python').text

soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')
print(f"amount of post:", len(articles)) 
# print(type(articles))
# print(articles)

# spans = soup.find_all('span', {'class': 'dib mt5'})
# for span in spans:
#     print(span.text)

article = articles[20]
post_url = article.find("a")
post_url= post_url.get("href")
  
img_url = article.find('img')
img = img_url.get("src")

position = article.find('h3').text
company = article.find('span', {'class': 'dib mt5'}).text
date = article.find('span', {'class': 'txt_list_2'}).text
salary = article.find('span', {'class': 'salary_amount'}).text
city = article.find('span', {'class': 'list_city'}).text

post = {
        "post_url": post_url, 
        "img_url": img,
        "position": position, 
        "company": company, 
        "salary": salary,
        "city": city,
        "date": date
        }
print(post)



# with open("out_data.json", "w") as outfile:
#     json.dump(out_posit_13,outfile)
#     json.dump(out_posit_14, outfile)
    
# with open("out_data.json", "w") as outfile:
#     json.dump(str_out, outfile, indent=3)
#     json.dump(out_posit_14, outfile)

# with open("out_data.json", "w") as outfile:
#     outfile.write(str_out)
#     json.dump(out_posit_14, outfile)



# with open('web_scrape.txt', 'w') as file:
#     file.write(out_posit_13)
#     file.write(out_posit_14)
#     print(f'Informacija irasyta faile ')

