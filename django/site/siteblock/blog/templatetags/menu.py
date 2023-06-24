from django import template
from blog.models import Category


register = template.Library()


@register.inclusion_tag("blog/menu_tpl.html")
def show_menu(menu_class="col-sm-4 offset-md-1 py-4"):
    category = Category.objects.all()
    return {"categories": category, "menu class": menu_class}