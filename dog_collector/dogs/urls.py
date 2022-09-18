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
    #Class Views Routes
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(),name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(),name='dogs_delete'),
    path('dogs/<int:dog_id>/add_trainer', views.add_trainer, name='add_trainer'),
]