from django.apps import AppConfig

from .Trie_data_structure import *
from django.conf import settings
import os

class ProfilesApiConfig(AppConfig):
    name = 'profiles_api'


    def ready(self):
        generate_1000()



top_1000 = Trie()
top_1000k = Trie()
def generate_1000():
    file_name = os.path.join(settings.BASE_DIR, 'top_1000.txt'),
    with open('top_1000.txt', 'r') as file:
        for line in file:
            top_1000.add_word(line.strip())

def generate_1000k():
    file_name = os.path.join(settings.BASE_DIR, 'top_1000.txt'),
    with open('top_1000.txt', 'r') as file:
        for line in file:
            top_1000.add_word(line.strip())

def get_top_1000():
    return top_1000

def get_top_1000k():
    return top_1000k
