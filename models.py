class Post:
    def __init__(self,
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
        self.time_now = time_now
        
        
    def data_dict(self):
        data = {  
            'post_id': post.post_id,
            'post_url': post.post_url,
            'position': post.position,
            'company': post.company,
            'city': post.city,
            'salary': post.salary,
            'upload_post': post.upload_post,           
            'applicants_value': post.applicants_value,
            'post_description_full': post.post_description_full,
            'post_date': post.post_date,
            'date_time_now': post.time_now,
        }
        return data


    def __str__(self):
        return f"post_description_full: {self.post_description_full}, post_id: {self.post_id}, post_url = {self.post_url}, position: {self.position}, company: {self.company}, city: {self.city}, salary: {self.salary}, upload_post: {self.upload_post}, post_date: {self.post_date}, applicants_value: {self.applicants_value}, time_now: {self.time_now}"
     

post = Post('1','2','3','4','5','6','7','8','9','10','11')
post1 = Post('a','b','c','d','i','f','g','h','j','k','l')
# print(x.city)
print(post.data_dict())
print(post1)        
