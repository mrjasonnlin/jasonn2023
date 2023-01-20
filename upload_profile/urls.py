from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'upload_profile'
urlpatterns = [
#    path('', include(('upload_profile.urls', 'upload_profile'), namespace='upload_profile')),
    path('upload_profile/', views.upload_profile, name='upload_profile'),
#    path('', views.upload_profile, name='upload_profile'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail, name='detail'),

]
