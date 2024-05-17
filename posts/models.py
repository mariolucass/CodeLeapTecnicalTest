from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=122)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=122)
    content = models.TextField()
