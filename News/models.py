from django.db import models

# Create your models here.
import datetime as dt
from ckeditor.fields import RichTextField

class tags(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    source = RichTextField(max_length = 100)
    title = models.CharField(max_length = 500)
    articleUrl = models.URLField(max_length =500)
    imageUrl = models.URLField(max_length = 500)
    date = RichTextField(max_length = 100)
    article = RichTextField()

    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def allnews(cls):
        # news = cls.objects.filter(pub_date__range=["2018-10-01", "2018-12-31"])
        news = cls.objects.filter().order_by('-id')[:500]
        return news

    @classmethod
    def search_by_title(cls,search_term):
        search_news = cls.objects.filter(title__icontains=search_term)
        return search_news




class Meta:
    ordering = ['name']
