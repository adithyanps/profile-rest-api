from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions
# Create your views here.
class HelloApiView(APIView):
    """test API view"""

    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post ,patch, put ,delete)',
        'it is similer to a traditional django view',
        'gives you the most control over your logic',
        'is mapped manualy to urls'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handles updating an object"""

        return Response({'method':'put'})
    def patch(self,requsest, pk=None):
        """patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,requsest,pk=None):
        """delete and object"""
        return Response({'method':'delete'})

class HelloViewset(viewsets.ViewSet):
    """test API viewset."""
    serializer_class = serializers.HelloSerializer
    def list(self,requset):
        """return a hello message"""
        a_viewset = [
        'uses actions(list,create ,retrieve,delete,update,partialupdate)',
        'automatically maps to URLs using Routers',
        'provides core functionality with less code.'
        ]

        return Response({'message':'hello','a_viewset':a_viewset})
    def create(self, request):
        """create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        """handles getting an object by its id"""
        return Response({'http_method':'GET'})
    def update(self, request, pk=None):
        """handles updating an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        """handles updating part of an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        """handles removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
class LoginViewset(viewsets.ViewSet):
    """checks email and password and return an auth token """

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use the ObtainAuthToken APIView to validate and create a token """
        return ObtainAuthToken().post(request)

class UserProfileFeedViewset(viewsets.ModelViewSet):
    """handles creating reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfilefeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
