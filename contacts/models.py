from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Comment model, related to User
    """
    email = models.CharField(max_length=254)  
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name