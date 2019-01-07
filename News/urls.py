from django.conf.urls import url
from News import views

urlpatterns=[
    url('^$',views.news, name = 'news'),
    url(r'^article/(?P<id>\d+)/', views.read_news_article, name="read_news_article"),
]
