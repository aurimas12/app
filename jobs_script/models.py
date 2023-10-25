class Post:
    def __init__(self,
                 id, 
                 url, 
                 img_url,
                 position, 
                 company, 
                 city, 
                 salary, 
                 post_date, 
                 upload_post, 
                 description, 
                 applicants_value):
        self.id = id
        self.url = url
        self.img_url = img_url
        self.position = position
        self.company = company
        self.city = city
        self.salary = salary
        self.upload_post = upload_post
        self.date = post_date
        self.description = description
        self.applicants_value = applicants_value
        
        
    def data_dict(self):
        data = {  
            'post_id': self.id,
            'post_url': self.url,
            'img_url': self.img_url,
            'position': self.position,
            'company': self.company,
            'city': self.city,
            'salary': self.salary,
            'post_date': self.date,
            'upload_post': self.upload_post,           
            'applicants_value': self.applicants_value,
            'description': self.description,
        }
        return data