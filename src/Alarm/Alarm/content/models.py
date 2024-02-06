from django.db import models

# Create your models here.
class Post(models.Model):
    number=models.TextField()   #번호
    title=models.TextField()    #제목
    date = models.TextField()   #날짜
    