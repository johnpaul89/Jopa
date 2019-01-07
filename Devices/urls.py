from django.conf.urls import url
from Devices import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.devices,name = 'devices'),
    # url(r'^specs/', views.phonespecs, name='phonespecs'),
    url(r'^specslike/$', views.specs_like_post, name='specs_like_post'),
    url(r'^specs/(?P<pk>\d+)/article/', views.specs_article, name='specs_article'),
    url(r'^reviews', views.phone_reviews, name='phone_reviews'),
    url(r'specs', views.phone_specs, name="phone_specs"),
    url(r'^review/(?P<pk>\d+)/article/', views.review_article, name='review_article'),
    url(r'^like/$', views.review_like_post, name='review_like_post'),

    url(r'^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
