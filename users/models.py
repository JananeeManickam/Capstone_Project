from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime

STATUS_CHOICES = (
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
)

class User(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = EmailField(unique=True, required=True)
    level = StringField(choices=["beginner", "intermediate", "advanced"], default="beginner")
    birthday = DateTimeField()
    
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'users'}
