from django.apps import AppConfig

from .Trie_data_structure import *
from django.conf import settings
import os

class ProfilesApiConfig(AppConfig):
    name = 'profiles_api'


    def ready(self):
        generate_1000()
        generate_1000k()
        generate_dictionary()



top_1000 = Trie()
top_1000k = set()
dictionary = set()


def generate_1000():
    # file_name = os.path.join(settings.BASE_DIR, 'top_1000.txt'),
    with open('top_1000.txt', 'r') as file:
        for line in file:
            top_1000.add_word(line.strip())
        file.close()

def generate_1000k():
    # file_name = os.path.join(settings.BASE_DIR, 'top_1000.txt'),
    with open('top_1000.txt', 'r') as file:
        words = []
        for line in file:
            # words.append(line.strip())
            top_1000k.add(line.strip())
        #     top_1000k.add_word(line.strip())
        # top_1000k = set(words)
        # print(top_1000k)
        file.close()

def generate_dictionary():
    # file_name = os.path.join(settings.BASE_DIR, 'top_1000.txt'),
    with open('clean_dictionary1.txt', 'r') as file:
        words = []
        for line in file:
            # print(line.strip(), '-----')
            dictionary.add(line.strip())
        #     top_1000k.add_word(line.strip())
        # dictionary = set(words)
        file.close()


def get_top_1000():
    return top_1000

def get_top_1000k():
    return top_1000k

def get_dictionary():
    return dictionary
