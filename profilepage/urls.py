from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile-detail'),
]