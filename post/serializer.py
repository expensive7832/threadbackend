from rest_framework import serializers
from .models import Post, PostImage, Likes
from django.contrib.auth import get_user_model
import cloudinary.uploader

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'id', 'img']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = PostImage
        fields = ['img', 'img_id']

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Likes
        fields = ['user' ]

class GetPostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    likes = LikePostSerializer(many=True)
    userId = UserProfileSerializer()
   
    
    class Meta:
        depth = 1
        model = Post
        fields = '__all__'
        


class createPostSerializer(serializers.Serializer):
    img_list = serializers.ListField(
        child=serializers.ImageField(),
        allow_empty = True,
        required=False,
        min_length = 0,
        max_length = 3
    )

    userId = serializers.CharField()
    body = serializers.CharField(default="")

        

    def create(self, data):
        
        userId = data['userId']
        body = data['body']

        

        try:
            

            user = User.objects.filter(id=userId).first()

            if user is None:
                raise ValueError("Authentication failed")
            

            else:
                newpost = Post.objects.create(userId = user,body = body)

                img_list = data.get('img_list')

                
                if img_list is not None:


                    for img in img_list:
                        result = cloudinary.uploader.upload(img)
                        print(result)
                        PostImage.objects.create( postid = newpost,img = result['secure_url'], img_id = result['public_id'])

                        return data
                else:

                    return data

        except BaseException as e:
            raise ValueError(str(e))