from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple categorir moddehe thake pare aber ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(User,on_delete=models.CASCADE) # many to one er jonno foreign key and cascade means author delete hole post o delete hobe

    def __str__(self):
        return self.title