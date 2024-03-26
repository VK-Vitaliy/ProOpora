from django.shortcuts import render
from goodsapp.models import Category


def index(request):
    ulichnye_opory = Category.objects.filter(name='Уличные опоры освещения')
    parkovye_opory = Category.objects.filter(name='Декоративные (парковые) опоры освещения')
    molnieotvody = Category.objects.filter(name='Молниеотводы')
    machty = Category.objects.filter(name='Мачты освещения и связи')
    kronshtejny = Category.objects.filter(name='Кронштейны, оголовники, короны')
    zdf = Category.objects.filter(name='Закладные детали фундаментов')
    komplektuyushie = Category.objects.filter(name='Комплектующие для опор, мачт, молниеотводов')

    context = {'title': 'ProOpora',
               'content': 'Торгово-производственная компания - ProOpora',
               'categories': [ulichnye_opory, parkovye_opory, molnieotvody, machty, kronshtejny, zdf, komplektuyushie],
               'index_flag': True,
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
