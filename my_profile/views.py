from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = profile.get_user_posts()
    return render(request, 'my_profile/profile_page.html', {'profile': profile, 'posts': posts})