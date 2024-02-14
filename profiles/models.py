from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.
class Edit_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    budget = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
