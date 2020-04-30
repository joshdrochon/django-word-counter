from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def countResult(request):
    full_text = request.GET['fulltext']
    world_list = full_text.split()

    word_dictionary = {}

    for word in world_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sortedWords = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'countResult.html', {'paramText': full_text, 'wordCount': len(world_list), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')