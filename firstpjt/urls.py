"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# urls.py 입장에서는 
# articles라는 패키지에서
# views라는 모듈을 가져오는 것
from articles import views

# app_name = 'articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('articles/<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
    path('number-print/<int:num>/', views.number, name ='number'),
    path('calculate/<int:num1>/<int:num2>/', views.calculate, name = 'calculate'),
]
