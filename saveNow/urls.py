from django.urls import path, include
from . import views

app_name = 'saveNow'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.createPost, name = 'create'),
]