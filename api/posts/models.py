from django.db import models
from api.company.models import Company    


class Tags(models.Model):
    language = models.CharField(max_length=40)
    
    def __str__(self):
        return self.language


class Description(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:100]
    # def __str__(self):
    #     return self.text


class Post(models.Model):
    register_id = models.IntegerField(null=True)  # post_id pervardinamas i register_id
    post_url = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    salary_min = models.IntegerField(null=True)
    salary_max = models.IntegerField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE, null=True, blank=True)
    # description = models.ForeignKey(Description, on_delete=models.SET_NULL, null=True, blank=True)
    download_datetime =  models.DateTimeField(auto_now_add=True)
    