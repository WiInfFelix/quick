from django.db import models

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField("date_published")
