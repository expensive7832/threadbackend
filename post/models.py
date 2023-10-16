from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]



class PostImage(models.Model):
    postid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    img = models.URLField(max_length=255, unique=True)
    img_id = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.img

class Likes(models.Model):
    postid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name="userlikeinfo")

    def __str__(self):
        return str(self.postid) + " " + self.user.first_name
    


