from .models import User
from rest_framework import serializers


class PhotoSerializer(serializers.Serializer):
    img = serializers.URLField()
    img_id = serializers.CharField()
    id = serializers.IntegerField()

    
    def create(self, data):
        user = User.objects.filter(id=data['id']).first()
        user.img = data['img']
        user.img_id = data['img_id']
        user.save()
        return data
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['img', 'username']

