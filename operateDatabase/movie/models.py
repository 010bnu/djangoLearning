from django.db import models

# Create your models here.
class Movie(models.Model):
    #电影名,年份,地区,剧情类型,导演,主演,评分,评论人数,简介
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    year  = models.CharField(max_length=100)
    area  = models.CharField(max_length=100)
    type  = models.CharField(max_length=100)
    doctor= models.CharField(max_length=100)
    stars = models.CharField(max_length=100)
    rate  = models.CharField(max_length=100)
    num   = models.CharField(max_length=100)
    desc  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title