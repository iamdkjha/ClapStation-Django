from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from posts.models import *
from home.models import *
from profiles.models import *

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def user_profile(request,email):
    if request.user.is_authenticated:
        try:
            profile = Edit_Profile.objects.get(user=User.objects.get(email=email))
        except ObjectDoesNotExist:
            profile = None
        use=User.objects.get(email=email)
        obj = Post.objects.filter(user=User.objects.get(email=email)).order_by('-id')
        try:
            add = Advertisement_section.objects.latest('created_at')
        except ObjectDoesNotExist:
            add = None
        return render(request,'profile.html', {'obj':obj, 'add':add, 'profile':profile,'user':use})
    else:
        return redirect('login')