from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import CommonMixin
from products.models import Basket, Product, ProductCategory


class IndexView(CommonMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'DESIREX Store'


class ProductsListView(CommonMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'DESIREX Store - Каталог'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        categories = cache.get("categories")
        if not categories:
            context["categories"] = ProductCategory.objects.all()
            cache.set("categories", context["categories"], 30)
        else:
            context["categories"] = categories
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
