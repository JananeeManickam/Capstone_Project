from datetime import timezone
from django.utils import timezone
from djongo import models

STATUS_CHOICES = (
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
)

class User(models.Model):
    """Main user model representing a user document in the 'users' collection."""
    _id = models.ObjectIdField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    level = models.CharField(max_length=50, choices=STATUS_CHOICES, default='beginner')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'