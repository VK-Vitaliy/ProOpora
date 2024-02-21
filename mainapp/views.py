from django.shortcuts import render
from goodsapp.models import Category


def index(request):
    categories = Category.objects.all()
    context = {'title': 'ProOpora',
               'content': 'Торгово-производственная компания - ProOpora',
               'categories': categories
               }

    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {'title': 'ProOpora',
               'content': 'О компании',
               'text_on_page': 'Торгово-производственная компания - ProOpora, '
                               'производство и поставка металлических опор '
                               'освещения, осветительных мачт и молниеотводов',
               }
    return render(request, 'mainapp/about.html', context)
