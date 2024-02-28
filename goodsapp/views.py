from django.shortcuts import render

from goodsapp.models import Product


def catalog(request):
    goods = Product.objects.all()
    context = {
        'title': 'ProOpora - catalog',
        'goods': goods
    }
    return render(request, 'goodsapp/catalog.html', context)


def product(request):
    return render(request, 'goodsapp/product.html')
