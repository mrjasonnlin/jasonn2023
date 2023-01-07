from django.urls import path
from . import views

app_name = 'upload'
urlpatterns = [
    path('', views.upload, name='upload'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),

]
