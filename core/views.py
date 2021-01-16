from django.shortcuts import render
import requests
from core.models import Word, Guess, lookup_word
from core.forms import GenerateGuess, DictionaryLookup
from django.conf import settings
from django.http import HttpResponseRedirect

# def lookup_word(search_word):
#     result = {}
#     endpoint = 'https://od-api.oxforddictionaries.com/api/v2/entries/{source_lang}/{word_id}'
#     url = endpoint.format(source_lang='en', word_id=search_word)
#     headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         result = response.json()
#         result['success'] = True
#     else:
#         result['success'] = False
#     if response.status_code == 404:
#         result['message'] = 'No entry found for "%s"' % search_word
#     else:
#         result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
#     return result

def index(request):
  words = Word.objects.all()
  new_word = Word.objects.create()
  context = {
    'words': words,
  }
  return render(request, 'index.html', context=context)

def word(request):
  current_word = Word.objects.last()
  LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  display_letters = []
  all_letters = []
  guessed_letters = []
  remaining_letters = len(current_word.word)
  guesses_remaining = 8

  for guess in Guess.objects.all():
    if guess.word.word == current_word.word:
      guessed_letters.append(guess.letter.upper())
      if guess.letter.upper() not in current_word.word:
        guesses_remaining -= 1
  
  for letter in current_word.word:
    all_letters.append(letter.upper())
    if letter in guessed_letters:
      display_letters.append(letter.upper())
      remaining_letters -= 1
    else:
      display_letters.append(' ')

  display_letters = f"{''.join(display_letters)}"
  all_letters = f"{''.join(all_letters)}"
  guessed_letters_string = f"{''.join(guessed_letters)}"
  LETTERS = f"{''.join(LETTERS)}"


  if request.GET.get('letterbox'):
    Guess.objects.create(word=current_word, letter=request.GET.get('letterbox'))
    return HttpResponseRedirect('/core/word/')

  context = {
    'current_word': current_word,
    'all_letters': all_letters,
    'display_letters': display_letters,
    'remaining_letters': remaining_letters,
    'guessed_letters': guessed_letters_string,
    'LETTERS': LETTERS,
    'guesses_remaining': guesses_remaining,
    'path': request.path,
  }

  return render(request, 'word/word.html', context=context)

def oxford(request):
  search_result = {}
  current_word = Word.objects.last().word.lower()
  search_result = lookup_word(current_word)

  context = {
    'search_result': search_result,
    'dict_word': current_word,
    }

  return render(request, 'oxford/oxford.html', context=context)