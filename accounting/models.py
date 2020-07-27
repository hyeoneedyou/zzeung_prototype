from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length= 50, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name="user")
    reason = models.TextField(null=True)
    base = models.TextField(null=True)
    experience = models.TextField(null=True)
    difficulty = models.TextField(null=True)
    recommend = models.TextField(null=True)
    content = models.TextField(null=True)
    view_count = models.IntegerField(default = 0, null=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    image = models.ImageField(upload_to='images/', null=True)

class Post2(models.Model):
    title = models.CharField(max_length= 50, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    reason = models.TextField(null=True)
    base = models.TextField(null=True)
    experience = models.TextField(null=True)
    difficulty = models.TextField(null=True)
    recommend = models.TextField(null=True)
    content = models.TextField(null=True)
    view_count = models.IntegerField(default = 0, null=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    image = models.ImageField(upload_to='images/', null=True)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)