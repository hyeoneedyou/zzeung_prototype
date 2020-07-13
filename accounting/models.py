from django.db import models

class Post(models.Model):
    title = models.CharField(max_length= 50, null=True)
    reason = models.TextField(null=True)
    base = models.TextField(null=True)
    experience = models.TextField(null=True)
    difficulty = models.TextField(null=True)
    recommend = models.TextField(null=True)
    content = models.TextField(null=True)
    view_count = models.IntegerField(default = 0, null=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)