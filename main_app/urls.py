from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.ToyCreate.as_view(), name='add'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='delete'),
]