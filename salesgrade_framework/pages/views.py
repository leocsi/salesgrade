from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader

# Create your views here.

def index(request):
    template= loader.get_template('pages/index.html')
    context= {}
    return HttpResponse(template.render(context, request))