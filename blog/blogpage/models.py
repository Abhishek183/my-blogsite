from django.db import models

# Create your models here.

class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    title=models.CharField(max_length=25)
    content=models.CharField(max_length=2000)
    slug=models.CharField(max_length=130)
    author=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author


