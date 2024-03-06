from django.db.models import Q

from goodsapp.models import Product


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    keyword = [word for word in query.split() if len(word) > 2]

    q_obj = Q()

    for token in keyword:
        q_obj |= Q(description__icontains=token)
        q_obj |= Q(name__icontains=token)

    return Product.objects.filter(q_obj)

