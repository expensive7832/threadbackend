from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seerializer import PhotoSerializer, UserSerializer
import cloudinary.uploader
from rest_framework.permissions import IsAuthenticated
from  rest_framework import status 
from .models import User
# Create your views here.

permisson_classes = [IsAuthenticated]
@api_view(['POST'])
def profilePhoto(request):
    try:
        user = request.user
        
        if user.is_anonymous:
            raise ValueError("Authentication failed")
        else:
            
            image = request.data.get("image")
            
            if image is None:
                raise ValueError("Upload Image")
            else:
                result = cloudinary.uploader.upload(image)
            
            request.data['id'] = user.id
            

            request.data['img_id'] = result['public_id']
            request.data['img'] = result['secure_url']
            request.data['id'] = user.id
        
            
            serializer = PhotoSerializer(data=request.data)

            if serializer.is_valid():
                 serializer.save()
                 return Response(data=serializer.data)
            else:
                 return Response(data=serializer.errors)
        
            
    

             
    except BaseException as e:
        return Response(str(e))



@api_view(['GET'])
def getUser(request, pk):
    
    try:
        user = User.objects.filter(id=pk).first()

        if user is None:
            raise ValueError("Authentication Needed")
        else:
            serializer = UserSerializer(user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
