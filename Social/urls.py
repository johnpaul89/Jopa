from django.conf.urls import url
from django.contrib import admin
from Social import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.social,name = 'social'),
    url(r'^accounts/profile/(?P<pk>\d+)/', views.update_profile, name="accountsprofilewithpk"),
    url(r'^accounts/edit-profile/', views.edit_profile , name='editprofile'),
    url(r'^accounts/change-password', views.change_password, name='changepassword'),
    url(r'^accounts/new-article', views.new_article, name='newarticle'),
    url(r'^article/(?P<pk>\d+)', views.read_article, name='readarticle'),
    url(r'^article/edit/(?P<id>\d+)/', views.edit_article, name='edit_article'),
    url(r'^article/delete/(?P<id>\d+)/', views.delete_article, name='delete_article'),
    url(r'^add/$', views.add, name='avatar_add'),
    url(r'^change/$', views.change, name='avatar_change'),
    url(r'^delete/$', views.delete, name='avatar_delete'),
    url(r'^like/$', views.like_post, name='like_post'),
    url(r'^accounts/profile/', views.super_profile, name="accountsprofile"),

    url(r'^cars/', views.cars_forum, name='carsforum'),
    url(r'^appswebsites/', views.apps_websites, name='appswebsites'),
    url(r'^general_discussion/', views.general_discussion, name='generaldiscussion'),
    url(r'^laptops/', views.laptops_forum, name='laptopsforum'),
    url(r'^offtopic/', views.off_topic, name='offtopic'),
    url(r'^operatingsystems/', views.operating_systems, name='operatingsystems'),
    url(r'^photographyvideography/', views.photography_videography, name='photographyvideography'),
    url(r'^programmes/', views.programmes_forum, name='programmesforum'),
    url(r'^smartphones_tablets/', views.smartphones_tablets, name='smartphonestablets'),
    url(r'^soundsystem/', views.sound_system, name='soundsystem'),
    url(r'^technews/', views.tech_news, name='technews'),
    url(r'^techtips/', views.tech_tips, name='techtips'),
    url(r'^televisions/', views.televisions_forum, name='televisionsforum'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
