from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.home, name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('mood/', include('mood.urls')),
    path('journal/', include('journal.urls')),
]
