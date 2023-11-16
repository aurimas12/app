from django.db import models
from api.company.models import Company    


class Tags(models.Model):
    language = models.CharField(max_length=40)


class Description(models.Model):
    text = models.TextField()
    

class Post(models.Model):
    register_id = models.IntegerField(null=True)  # post_id keiciamas i register_id
    post_url = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    salary_min = models.IntegerField(null=True)
    salary_max = models.IntegerField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    # Add foreign key to Company, Tags, Description model with default value
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, default=1)
    description = models.ForeignKey(Description, on_delete=models.CASCADE, default=1)





    
# class Postsfull(models.Model):
#     company_info = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)  # 'app_label.CompanyInfo'
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 'app_label.Post'

    # salary = models.JSONField(default=list)
    # salary = models.DecimalField(max_digits=15, decimal_places=2, default=0, default_currency='EUR')
    
    # position = models.CharField(max_length=10)
    # applicants_value = models.SmallIntegerField()
    # posts_full = models.ForeignKey(Postsfull, on_delete=models.CASCADE)



