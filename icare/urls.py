"""icare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from pages import views
urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^about/(?P<pk>\d+)/$', views.about, name='about'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('work', views.our_work, name='our_work'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('icare/admin/', admin.site.urls),
    path('base', views.base, name='base'),
    path('contact', views.base, name='base'), # base will be deleted
    url(r'^references', views.references, name='references'),

]
