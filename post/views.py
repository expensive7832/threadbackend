from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import createPostSerializer, GetPostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
import json
# Create your views here.

@api_view(['GET'])
def GetPosts(request):

    all_post = Post.objects.all().order_by("-datePosted")

    serializer = GetPostSerializer(all_post, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


permission_classes = [IsAuthenticated]
@api_view(['POST'])

def CreatePost(request):
    
    try:
        user = request.user
        
        
        if user.is_anonymous:
           
            raise ValueError("authentication failed")
    
        else:
           
            request.data._mutable = True
            
            request.data['userId'] = user.id

            serializer = createPostSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    except BaseException as e:
        return Response(data=str(e))
