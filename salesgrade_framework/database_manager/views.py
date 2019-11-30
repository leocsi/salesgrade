from django.shortcuts import render
from django.http import HttpResponse
from database_manager.models import Name, Age
from django.template import loader


# Create your views here.
def database_view(request):
    template = loader.get_template('database_manager/database_view.html')
    context = {}
    return HttpResponse(template.render(context,request))

def own_results(request, user_name):
    if (user_name != 'index'):
        return HttpResponse('here are your own results, dear %s ' % user_name)
    else: 
        raise Exception

def same_age(request, user_age):
    return HttpResponse("Here is everyone who is %s " %user_age + "years old")