from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('escape/', views.logout),
]
