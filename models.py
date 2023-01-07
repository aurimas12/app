class Post:
    def __init__(self,
                 id, 
                 url, 
                 position, 
                 company, 
                 city, salary, 
                 upload_post, 
                 create_date, 
                 description_full, 
                 applicants_value, 
                 time_now):
        self.description_full = description_full
        self.id = id
        self.url = url
        self.position = position
        self.company = company
        self.city = city
        self.salary = salary
        self.upload_post = upload_post
        self.date = create_date
        self.applicants_value = applicants_value
        self.time_now = time_now
        
        
    def data_dict(self):
        data = {  
            'post_id': self.id,
            'post_url': self.url,
            'position': self.position,
            'company': self.company,
            'city': self.city,
            'salary': self.salary,
            'upload_post': self.upload_post,           
            'applicants_value': self.applicants_value,
            'post_description_full': self.description_full,
            'post_date': self.create_date,
            'date_time_now': self.time_now,
        }
        return data


    def __str__(self):
        return f"post_description_full: {self.description_full}, post_id: {self.id}, post_url = {self.url}, position: {self.position}, company: {self.company}, city: {self.city}, salary: {self.salary}, upload_post: {self.upload_post}, post_date: {self.post_date}, applicants_value: {self.applicants_value}, time_now: {self.time_now}"
     

post = Post('1','2','3','4','5','6','7','8','9','10','11')
post1 = Post('a','b','c','d','i','f','g','h','j','k','l')

