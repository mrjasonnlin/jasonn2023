from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include('render.urls')),
    path('', views.index, name='index'),
#    path('main/', include('main.urls')),
    path('about/', views.about, name='about'),
    path('bike/', views.bike, name='bike'),
    path('django/', views.django, name='django'),
    path('main/', views.main, name='main'),
    path('users/', views.users, name='users'),
]

