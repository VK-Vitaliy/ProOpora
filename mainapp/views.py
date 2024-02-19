from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': 'Home',
               'content': 'Main page - Shop Home',
               }

    return render(request, template_name='mainapp/index.html', context=context)


def about(request):
    return HttpResponse("О компании ProOpora")
