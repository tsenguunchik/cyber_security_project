from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import apps

# from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    # serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        a = request.GET.get('password', '')

        top_1000 = apps.get_top_1000()

        if top_1000.contains(a, True):
            return Response({'message': 'Password is weak'})
        else:
            return Response({'message': 'Password is okay'})

    # def post(self, request):
    #     """Create a hello message with our name."""
    #
    #     serializer = serializers.HelloSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         name = serializer.data.get('name')
    #         message = 'Hello {0}'.format(name)
    #         return Response({'message': message})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request, pk=None):
    #     """Handles updating an object. update!"""
    #
    #     return Response({'method': 'put'})
    #
    # def patch(self, request, pk=None):
    #     """Patch request, only updates fields provided in the request"""
    #
    #     return Response({'method': 'patch'})
    #
    # def delete(self, request, pk=None):
    #     """Deletes an object."""
    #
    #     return Response({'method': 'delete'})
