"""Warsztaty_3 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

# from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from Box.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),   
          
    url(r'^$', ShowAll.as_view()),    
     
    url(r'^new_person/$', csrf_exempt(NewPerson.as_view())),
    url(r'^modify_person/(?P<id>\d+)$',csrf_exempt(ModifyPerson.as_view())),
    url(r'^delete_person/(?P<id>\d+)$',csrf_exempt (DeletePerson.as_view())),
    url(r'^show_person/(?P<id>\d+)$',csrf_exempt (ShowPerson.as_view())),
     
    url(r'^(?P<id>\d+)/add_address/$', csrf_exempt(AddAddress.as_view())),
    url(r'^(?P<id>\d+)/add_telephone/$',csrf_exempt (AddTelephone.as_view())),
    url(r'^(?P<id>\d+)/add_email/$',csrf_exempt(AddEmail.as_view())),

]
