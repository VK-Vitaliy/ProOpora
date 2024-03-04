from django.shortcuts import render

from goodsapp.models import Product


def catalog(request):
    goods = Product.objects.all()
    context = {
        'title': 'ProOpora - catalog',
        'goods': goods
    }
    return render(request, 'goodsapp/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, 'goodsapp/product.html', context=context)
