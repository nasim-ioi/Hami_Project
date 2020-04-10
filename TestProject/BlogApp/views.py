from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework import status

from .models import Blog
from .serializers import UserSerializer, BlogSerializer


class Signup(APIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'you signed up successfully'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BlogViewSet(ModelViewSet):
    """
    create :  
        creating a Blog object by an authenticated user
    
    list :
        displaying all the Blog objects to an authenticated user
    
    retreive :
        displaying a specific Blog object to an authenticated user
    
    update :
        updating a specific Blog object information by an authenticated user
    
    partial_update :
        partial updating a specific Blog object information by an authenticated user
    
    destroy :
        deleting a specific Blog object by an authenticated user

    """

    # only athenticated users(which have logged in) can create, read, update or delete their blog
    permission_classes = [IsAuthenticated]

    # each authenticated user can up to 10 rates in a minute request to this view
    throttle_classes = [UserRateThrottle]

    queryset = Blog.objects.all()

    serializer_class = BlogSerializer
