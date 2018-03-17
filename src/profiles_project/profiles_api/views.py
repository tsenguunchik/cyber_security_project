from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from . import apps

# from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    # serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""
        start_time = time.time()
        sent_password = request.GET.get('password', '')

        trie_tree = apps.get_top_1000()
        password_set = {}
        response = {}

        if trie_tree.contains(sent_password, True):
            response = {'is_safe': 'No', 'message':'The password is in top 1,000 most common passwords'}
        elif trie_tree.contains(sent_password, False):
            response = {'is_safe': 'No', 'message':'The password is prefix of 1,000 most common passwords'}
        else:
            password_set = apps.get_top_1000k()
            # print(password_set)
            if sent_password in password_set:
                response = {'is_safe': 'No', 'message':'The password is in top 1,000,000 most common passwords'}
            else:
                password_set = apps.get_dictionary()
                # print(password_set)
                if sent_password in password_set:
                    response = {'is_safe': 'No', 'message':'Found in dictionary'}
                else:
                    response = {'is_safe': 'Yes', 'message': 'Password was not found in database'}

        response['time'] = str(int((time.time() - start_time) * 1000000)) + ' us'
        return Response(response)
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
