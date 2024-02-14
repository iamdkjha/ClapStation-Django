from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.unregister(Group)