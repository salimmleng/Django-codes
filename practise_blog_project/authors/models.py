from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    author_name = models.CharField(max_length=30)
    bio = models.TextField()
    phone_no = models.IntegerField()