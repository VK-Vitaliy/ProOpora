from django.shortcuts import render, get_list_or_404

from goodsapp.models import Product


def catalog(request, category_slug):
    goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
    context = {
        'title': 'ProOpora - catalog',
        'goods': goods
    }
    return render(request, 'goodsapp/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, 'goodsapp/product.html', context=context)
