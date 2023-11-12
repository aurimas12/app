from django.db import models
from api.company.models import Company    


class Post(models.Model):
    register_id = models.CharField(max_length=40)  # post_id keiciamas i register_id
    post_url = models.CharField(max_length=200)
    upload_post = models.CharField(max_length=50)
    salary = models.SmallIntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True,)
    # Add foreign key to Company model with a default value
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    

class Tags(models.Model):
    language = models.CharField(max_length=40)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)


class Description(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)


class Position(models.Model):
    position = models.CharField(max_length=10)
    applicants_value = models.SmallIntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    
    
    
    

# class Postsfull(models.Model):
#     company_info = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)  # 'app_label.CompanyInfo'
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 'app_label.Post'

    # salary = models.JSONField(default=list)
    # salary = models.DecimalField(max_digits=15, decimal_places=2, default=0, default_currency='EUR')
    
    # position = models.CharField(max_length=10)
    # applicants_value = models.SmallIntegerField()
    # posts_full = models.ForeignKey(Postsfull, on_delete=models.CASCADE)



