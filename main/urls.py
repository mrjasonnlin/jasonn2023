from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('bike/', views.bike, name='bike'),
]