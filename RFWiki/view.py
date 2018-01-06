from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {'text': "put dynamic text here"}
    return render(request, 'key_word.html', context)
