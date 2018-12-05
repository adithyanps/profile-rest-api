from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
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
