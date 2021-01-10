from django import template
from ..models import Category
register=template.Library()

@register.simple_tag
def title():
    return "وبی لاگی ، جنگو محور"

@register.inclusion_tag("partials/category_navbar.html")
def category_navbar():
    return {
        "category":Category.objects.filter(status=True)
    }
