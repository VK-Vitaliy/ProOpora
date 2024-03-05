from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goodsapp.models import Product


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    page = request.GET.get('page', 1)
    paginator = Paginator(goods, per_page=6)
    current_page = paginator.page(int(page))
    context = {
        'title': 'ProOpora - catalog',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goodsapp/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, 'goodsapp/product.html', context=context)
