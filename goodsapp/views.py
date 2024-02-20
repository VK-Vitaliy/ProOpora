from django.shortcuts import render


def catalog(request):
    return render(request, 'goodsapp/catalog.html')


def product(request):
    return render(request, 'goodsapp/product.html')
