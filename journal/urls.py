from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.journal_list, name='journal_list'),
    path('entries/new/', views.journal_create, name='journal_create'),
    path('entries/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('entries/<int:pk>/edit/', views.journal_update, name='journal_update'),
    path('entries/<int:pk>/delete/', views.journal_delete, name='journal_delete'),
]
