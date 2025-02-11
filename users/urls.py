from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.users_api),  # List all users or create a user
    path('users/<int:id>/', views.users_api),  # Get/update/delete user by ID
]
