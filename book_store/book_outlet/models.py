from django.db import models

# Create your models here.
#models are the tables in the database, where we define the columns and entities

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    # id = models.AutoField(primary_key=True) this is the default primary key