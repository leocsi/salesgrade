from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader
from database_manager import templates

# Create your views here.

def index(request):
    template= loader.get_template('C:\\Users\\Asus\\Google Drive\\Info\\Salesgrade\\salesgrade_framework\\templates\\pages\\frame.html')
    context= {}
    return HttpResponse(template.render(context, request))