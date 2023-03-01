from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('my/', views.detail_active, name='profile_detail_active'),
]
