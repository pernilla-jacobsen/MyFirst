from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='cat-home'),
    path('about/', views.about, name='cat-about'),
]
