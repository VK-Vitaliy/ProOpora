from django.shortcuts import render
from goodsapp.models import Category


def index(request):
    ulichnye_opory = Category.objects.filter(pk=1)
    parkovye_opory = Category.objects.filter(pk=2)
    molnieotvody = Category.objects.filter(pk=3)
    machty = Category.objects.filter(pk=4)
    kronshtejny = Category.objects.filter(pk=5)
    zdf = Category.objects.filter(pk=6)
    komplektuyushie = Category.objects.filter(pk=7)

    context = {'title': 'ProOpora',
               'content': 'Торгово-производственная компания - ProOpora',
               'categories': [ulichnye_opory, parkovye_opory, molnieotvody, machty, kronshtejny, zdf, komplektuyushie]
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
