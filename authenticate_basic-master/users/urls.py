from django.urls import path, include
from . import views
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='home'),
    path('children', views.children, name='children'),
    path('register/', Register.as_view(), name='register'),
    path('profile', views.Profile, name='profile'),
    path('support', views.support, name='support'),
    path('send', views.send, name='send'),
    path('choose', views.choose, name='choose'),
    path('teen', views.teen, name='teen'),
    path('disk', views.disk, name='disk'),
]
