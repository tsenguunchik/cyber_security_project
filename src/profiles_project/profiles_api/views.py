from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response




# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses Http methods as function (get, post, patch, put, delete)',
            'its similar to a traditional django view',
            'is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        
