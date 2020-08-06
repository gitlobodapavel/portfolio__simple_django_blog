from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<int:pk>', views.post, name='homepage'),
    path('search/', views.search, name='search'),
]