from django.urls import path
from .views import profilePhoto, getUser

urlpatterns = [
    path("upload/", profilePhoto),
    path("userdata/<int:pk>", getUser),

]