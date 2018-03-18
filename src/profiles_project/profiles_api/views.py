from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from . import apps
import random
# from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    # serializer_class = serializers.HelloSerializer


    def check_password(self, sent_password):
        start_time = time.time()


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
        return response

    def change_password(self, password, type, number, tries):
        new_password = list(password)
        try:
            number = int(number)
        except:
            return {'error': 'Number must be integer'}
        if 1 > number or number > 10:
            return {'error': 'Number must be from 1 to 10'}
        all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$^*().,0123456789'
        numbers_chars = '0123456789'
        alpha_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        special_chars = '!@$^*().,'
        tries = tries + 1
        if type == 'insert':
            for i in range(number):
                new_password.insert(random.randint(0, len(new_password)), random.choice(all_chars))
        elif type == 'replace':
            for i in range(number):
                new_password[random.randint(0, len(new_password) - 1)] = random.choice(all_chars)
        else:
            return {'error': 'Unknown Type'}

        new_password = ''.join(new_password)


        if self.check_password(new_password)['is_safe'] == 'Yes':
            return {'new_password': new_password, 'tries': str(tries), 'is_safe': 'Yes'}
        else:
            while self.check_password(new_password)['is_safe'] == 'No' and tries < 10:
                tries += 1
                new_password = self.change_password(password, type, number, tries)['new_password']
            if tries == 10:
                return {'new_password': new_password, 'tries': str(tries), 'is_safe': 'No'}
            else:
                return {'new_password': new_password, 'tries': str(tries), 'is_safe': 'Yes'}


    def get(self, request, format=None):
        """Returns a list of APIView features."""

        sent_password = request.GET.get('password', '')
        type = request.GET.get('type', '')
        number = request.GET.get('number', '')
        response = {}
        if type == '' and number == '':
            response = self.check_password(sent_password)
        else:
            response = self.change_password(sent_password, type, number, 0)

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
