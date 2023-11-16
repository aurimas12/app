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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
