from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    Category = (
        ("1", "Travel"),
        ("2", "Programming"),
        ("3", "Beauty"),
        ("4", "Healt"),
        ("5", "Spor"),
        ("6", "Other"),
    )
    Status = (
        ("D", "Draft"),
        ("V", "View"),
    )
    category = models.CharField(max_length=20, choices=Category, default='6')
    status = models.CharField(max_length=6, choices=Status, default='D')
    def __str__(self):
        return f"{self.user} {self.title}"
class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=250)
    dateTime = models.DateTimeField(default=now)
    def __str__(self):
        return f'{self.user}{self.body}'
class Like(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='likes',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} {self.blog}'
class BlogView(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='views',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} {self.blog}'