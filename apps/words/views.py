# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.

def index(request):
    if 'list' not in request.session:
        request.session['list'] = []
    return render (request, 'words/index.html')


def process(request): 
    color = ''
    if 'color' in request.POST:
        color = request.POST['color']

    time = strftime('%H:%M %p %m-%d-%Y', gmtime())
    
    bold = ''
    if 'bold' in request.POST:
        bold = request.POST['bold']
    
    dict2 = {
        'word2' : request.POST['word'],
        'color2' : color,
        'bold' : bold,
        'time': time
    }

    temp = request.session['list']
    temp.append(dict2)
    request.session['list'] = temp
    request.session.modified == True
    # request.session["word"] = request.session["words"].append(word)
    return redirect ('/') 

def reset(request):
    request.session.clear()
    return redirect('/')