from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """test API view"""
    def get(self,request,format=None):
        """returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post ,patch, put ,delete)',
        'it is similer to a traditional django view',
        'gives you the most control over your logic',
        'is mapped manualy to urls'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
