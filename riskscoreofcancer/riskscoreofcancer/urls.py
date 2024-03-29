"""
URL configuration for riskscoreofcancer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from riskscoreapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('insert/',views.insert_view),
    path('insert/home.html',views.home),
    path('display/',views.display_view),
    # path('update/',views.update1_view),
    # path('update1/',views.update_view),
    path('search/',views.search_view),
    path('delete/',views.delete_view),
    path('search/home.html',views.home)
]