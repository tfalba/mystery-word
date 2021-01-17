from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
#from core.forms import DictionaryLookup
from django.conf import settings

import os
import random
import requests

#text_path = os.path.join(settings.BASE_DIR, 'core/words.txt')
text_path = os.path.join(settings.BASE_DIR, 'core/words2.txt')
ALL_WORDS = open(text_path, 'r').read().lower()

# ALL_WORDS = open('/Users/tracyfalba/momentum/django-projects/locallibrary/catalog/words.txt', 'r').read().lower()
ALL_WORDS = ALL_WORDS.split()
ALL_SMALL_WORDS = []
for word in ALL_WORDS:
    if len(word) in range(4,9):
        ALL_SMALL_WORDS.append(word)


def lookup_word(search_word):
    result = {}
    endpoint = 'https://od-api.oxforddictionaries.com/api/v2/entries/{source_lang}/{word_id}'
    url = endpoint.format(source_lang='en', word_id=search_word)
    headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        result['success'] = True
    else:
        result['success'] = False
    if response.status_code == 404:
        result['message'] = 'No entry found for "%s"' % search_word
    else:
        result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
    return result

def word_default():
    word_is_good = False
    
    while word_is_good == False:
        search_result = {}
        current_word = random.choice(ALL_SMALL_WORDS).lower()
        #form = DictionaryLookup()
        search_result = lookup_word(current_word)
        if search_result['success']==True:
            word_is_good = True
            return current_word.upper()


class Word(models.Model):
    word = models.CharField(max_length=25, default=word_default)

    def __str__(self):
        return f'{self.word}'

    def get_absolute_url(self):
        return reverse('word-detail', args=[str(self.id)])


class Guess(models.Model):
    word = models.ForeignKey('Word', on_delete=models.SET_NULL, null=True)
    letter = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.letter}'


class User(AbstractUser):
    pass
