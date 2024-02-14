import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()


# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    postContent = models.CharField(max_length=500, blank=True)
    postImage = models.FileField(null=True, blank=True, upload_to='images/')
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user} : {self.postContent}"
    
    class Meta:
        ordering = ['-created_at']
    

class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.email} : {self.post.postContent}'