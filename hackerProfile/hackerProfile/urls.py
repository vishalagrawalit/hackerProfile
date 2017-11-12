"""hackerProfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from Profile.views import hackerform, update, index, skillform, editbasicInfo, editskills, errorpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', index),
    url(r'^create/$', hackerform),
    url(r'^create/(?P<id>\d+)/(?P<user>[\w.@+-]+)/$', skillform),
    url(r'^edit/basic_info/(?P<id>\d+)/(?P<user>[\w.@+-]+)/$', editbasicInfo),
    url(r'^edit/skills/(?P<id>\d+)/(?P<user>[\w.@+-]+)/$', editskills),
    url(r'^profile/(?P<id>\d+)/$', update),
    url(r'^error/$', errorpage),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)