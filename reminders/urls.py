from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('toggle/<int:pk>/', views.reminder_toggle, name='reminder_toggle'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
]
