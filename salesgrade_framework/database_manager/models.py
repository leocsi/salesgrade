from django.db import models

# Create your models here.

class Name(models.Model):
    user_name = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

class Age(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    user_age = models.IntegerField(default='N/I')
