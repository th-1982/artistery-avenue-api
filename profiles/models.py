from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../profile_mgdafv'
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """Return string"""
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """Creates profile when a new user is created"""
    if created:
        Profile.objects.create(owner=instance)


# signal to listen for when a new user is saved
# and create the profile
post_save.connect(create_profile, sender=User)



