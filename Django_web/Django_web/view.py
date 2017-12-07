#!/use/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
#from django.http import HttpResponse

def hello(request):
    context = {}
    context['hello'] = 'This is test words!'
    return render(request, 'hello.html', context)
