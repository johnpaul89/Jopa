from django.contrib import admin
from .models import NewsArticle, tags

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(tags)
