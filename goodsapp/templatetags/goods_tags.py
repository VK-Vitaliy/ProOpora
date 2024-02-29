from django import template

from goodsapp.models import Category

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Category.objects.all()
