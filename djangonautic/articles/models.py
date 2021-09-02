from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True) #auto_now_add=True means when a new entry is create it automatically is assigned the current time.
    thumb=models.ImageField()
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    no_of_likes=models.PositiveIntegerField(default=0)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.body

    def get_comments(self):
        return reversed(self.comments_set.order_by('-time')[:3])

class Likes(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE)
    person=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person.username) + ' likes the post with id ' + str(self.post.id)

class Comments(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE)
    person=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.person.username) +': '+str(self.text) +' on post'+ str(self.post.id)
