from django import template

from apps.products.model import GroupCategories

register = template.Library()


@register.inclusion_tag("componentns/header.html")
def header() -> dict:
    group_categories = GroupCategories.objects.prefetch_related("category")

    return {
        "group_categories": group_categories,
    }
