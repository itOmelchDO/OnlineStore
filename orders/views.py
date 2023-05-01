from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from common.views import CommonMixin
from orders.forms import OrderForm


class OrderCreateView(CommonMixin, CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:order_create")
    title = "DESIREX - Оформлення замовлення"
