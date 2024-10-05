from email.mime import image
from email.policy import default
from sqlite3 import Timestamp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from myapp import static
from myapp.static import modify

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.CharField(max_length=60)
    slug = models.CharField(max_length=130)
    timestamp= models.DateTimeField(default=now)


    def __str__(self):
        return self.title + ' by '+ self.author

class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    content = models.TextField()
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return 'Message From '+ self.name

class blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE , null= True)
    timestamp= models.DateTimeField(default=now)

    def __str__(self) :
        return self.comment[0:13] + "... " + "by " + self.user.username 
