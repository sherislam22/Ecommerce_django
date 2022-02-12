from django.contrib import admin
from .models import Products, Category, Tags
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Tags)