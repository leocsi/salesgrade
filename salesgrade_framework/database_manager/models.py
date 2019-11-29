import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Name(models.Model):
    user_name = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    def __str__(self):
        return self.user_name
    def was_published_recently(self):
        return self.publication_date >= timezone.now() - datetime.timedelta(days=1)

class Age(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    user_age = models.IntegerField(default='N/I')
    def __str__(self):
        return str(self.user_age)
