from django.urls import path
from .views import (
    CatListView,
    CatDetailView,
    CatCreateView, 
    CatUpdateView,
    CatDeleteView
)
from . import views


urlpatterns = [
    path('', CatListView.as_view(), name='cat-home'),
    path('cat/<int:pk>/', CatDetailView.as_view(), name='cat-detail'),
    path('new',CatCreateView.as_view(), name='cat-create'),
    path('cat/<int:pk>/update/', CatUpdateView.as_view(), name='cat-update'),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view(), name='cat-delete'),
    path('about/', views.about, name='cat-about'),
]
