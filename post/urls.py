from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.urls import path
from . import views



urlpatterns = [
    path("all_post/", views.GetPosts),
    path("create_post/", views.CreatePost),
]
