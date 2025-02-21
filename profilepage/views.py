from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profilepage/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(user__username=self.kwargs['username'])