
from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
# Category 
# Product
# Tag

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    category_image = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return self.name

    
class Products(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    products_image = models.ImageField(upload_to='products_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ForeignKey('Tags', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self) -> str:
        return f'{self.id} {self.name}'
    

class Tags(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
