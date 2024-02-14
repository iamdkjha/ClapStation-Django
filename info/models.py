from django.db import models

# Create your models here.
class ContactUs(models.Model):
        
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.name