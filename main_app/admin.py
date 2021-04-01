from django.contrib import admin

from .models import Pin, Comment, Category

# Register your models here.
admin.site.register(Pin)
admin.site.register(Comment)
admin.site.register(Category)