from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_mood, name='log_mood'),
    path('history/', views.mood_history, name='mood_history'),
    path('export/', views.export_mood_pdf, name='export_mood_pdf'),
]
