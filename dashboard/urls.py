from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('wellness/', views.wellness, name='wellness'),
]
