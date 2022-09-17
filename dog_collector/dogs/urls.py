from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #General Routes
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #Dog Routes
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
]