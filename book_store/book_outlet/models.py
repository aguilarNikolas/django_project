from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
#models are the tables in the database, where we define the columns and entities
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)
    # id = models.AutoField(primary_key=True) #this is the default primary key
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #db_index is for faster queries


    def __str__(self):
        return f"{self.title} - {self.author} - {self.rating}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # this is a pre-save method that is called before the object is saved to the database
    # it has been removed because we are using the slugify field in the admin panel
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
