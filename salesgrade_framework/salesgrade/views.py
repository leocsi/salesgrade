from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader


# Create your views here.
def Test(request):
    template = loader.get_template('self_assessment/1_prof_comm.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Index(request):
    template= loader.get_template('salesgrade/index.html')
    context= {}
    return HttpResponse(template.render(context, request))