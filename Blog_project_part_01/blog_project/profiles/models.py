from django.db import models
from authors.models import Author
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    # one to one relationship 
    author = models.OneToOneField(Author,on_delete=models.CASCADE, default= None)

    def __str__(self):
        return self.name