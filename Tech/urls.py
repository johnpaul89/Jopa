from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Social import views

from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'',include('Devices.urls')),
    url(r'^news/',include('News.urls')),
    url(r'^social/',include('Social.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login', views.login_view, name='login'),
    url(r'^accounts/logout', views.logout_view, name='logout'),
    url('avatar/', include('avatar.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^auth/', include('social_django.urls', namespace='socialauth')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
