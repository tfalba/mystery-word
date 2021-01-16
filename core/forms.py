from django import forms
#from core.models import Word
from django.conf import settings
import requests
import json

# -------------------------------------------- No longer using this either ------------------------------------------- #

class GenerateGuess(forms.Form):
  next_guess = forms.CharField(max_length=1)

  def cleaned_guess_data(self):
    data = self.cleaned_data['next_guess']
    return data

# -------------------- Below is not used anymore as wrote this as a function in models and views. -------------------- #

class DictionaryLookup(forms.Form):
  dict_word = forms.CharField(max_length=50, required=False)
  
  def search(self, search_word):
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







