from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include('render.urls')),
#    path('', views.main, name='main'),
#    path('main/', include('main.urls')),
#    path('about/', views.about, name='about'),
#    path('bike/', views.bike, name='bike'),
]

