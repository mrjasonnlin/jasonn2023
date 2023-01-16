from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(('main.urls', 'main'), namespace='main')),
#    path('', include(('account.urls', 'account'), namespace='account'))
#    path('', include(('register.urls', 'register'), namespace='register')),
#    path('', include(('login.urls', 'login'), namespace='login')),
#    path('', include(('logout.urls', 'logout'), namespace='logout'))
#    path('register/', views.register, name='register'),
#    path('login/', views.login, name='login'),
#    path('logout/', views.register, name='logout'),

]