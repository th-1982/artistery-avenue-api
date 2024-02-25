from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):
    post = models.ForeignKey(Post, related_name='bookmarks',
                             on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = [['owner', 'post']]

    def __str__(self):
        return f"{self.owner} {self.post}"
