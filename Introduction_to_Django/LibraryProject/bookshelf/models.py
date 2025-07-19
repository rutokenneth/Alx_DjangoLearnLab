from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title:} by {self.author}"
