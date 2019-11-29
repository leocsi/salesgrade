from django.shortcuts import render
from django.http import HttpResponse
from database_manager.models import Name, Age
from django.template import loader


# Create your views here.

def index(request):
    latest_name_list = Name.objects.order_by('-publication_date')[:5]
    template = loader.get_template('database_manager/index.html')
    context = {
        'latest_name_list': latest_name_list,
    }
    return HttpResponse(template.render(context, request))

def own_results(request, user_name):
    template= loader.get_template('database_manager/own_results.html')
    context= {}
    return HttpResponse(template.render(context, request))
def same_age(request, user_age):
    return HttpResponse("Here is everyone who is %s " %user_age + "years old")