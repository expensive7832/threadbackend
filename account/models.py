from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomizeUser
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    img = models.URLField(max_length=255, unique=True, null=True)
    img_id = models.CharField(max_length=255, unique=True, null=True)
    gender = models.CharField(max_length=5, default='male')
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name","gender", "username"]

    objects = CustomizeUser()

    

    def __str__(self):
        return self.email
    

class Followers(models.Model):
    accid = models.ForeignKey(User, related_name="account_id", on_delete=models.CASCADE)
    followerid = models.ForeignKey(User, related_name="follower_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.accid + " " + self.followerid

class Follow(models.Model):
    accid = models.ForeignKey(User,  related_name="acc_id" , on_delete=models.CASCADE)
    followid = models.ForeignKey(User, related_name="followid", on_delete=models.CASCADE)


