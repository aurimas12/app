class Post:
    def __init__(self, count_all_posts, 
                 count_all_pages, 
                 post_id, 
                 post_url, 
                 position, 
                 company, 
                 city, salary, 
                 upload_post, 
                 post_date, 
                 post_description_full, 
                 applicants_value, 
                 time_now):
        self.count_all_posts = count_all_posts
        self.count_all_pages = count_all_pages
        self.post_description_full = post_description_full
        self.post_id = post_id
        self.post_url = post_url
        self.position = position
        self.company = company
        self.city = city
        self.salary = salary
        self.upload_post = upload_post
        self.post_date = post_date
        self.applicants_value = applicants_value
        self.date_time_now = time_now
        
        
# Kol kas padariau tik inicializacija bandau aiskintis ir pasimokint classes