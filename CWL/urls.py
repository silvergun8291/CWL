"""
URL configuration for CWL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index, name='index'),
    path('index.html', views.index),
    path('why/', views.why),
    path('why.html', views.why),
    path('about/', views.about),
    path('about.html', views.about),
    path('tracking/', views.tracking, name='tracking'),
    path('tracking.html', views.tracking, name='tracking'),
    path('privacy/', views.privacy),
    path('privacy.html', views.privacy),
    path('detail.html', views.detail),
    path('detail/', views.detail, name='detail'),
]
