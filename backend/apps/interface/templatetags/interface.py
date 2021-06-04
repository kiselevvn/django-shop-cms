from django import template

from apps.products.models import GroupCategories

register = template.Library()


@register.inclusion_tag("components/header.html")
def header(user) -> dict:
    group_categories = GroupCategories.objects.all()

    return {
        "user": user,
        "group_categories": group_categories,
    }
