import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.conf import settings

from common.views import CommonMixin
from orders.forms import OrderForm

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(CommonMixin, TemplateView):
    template_name = "orders/success.html"
    title = "DESIREX - Дякуємо за покупку!"


class CanceledTemplateView(TemplateView):
    template_name = "orders/canceled.html"


class OrderCreateView(CommonMixin, CreateView):
    template_name = "orders/order-create.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:order_create")
    title = "DESIREX - Оформлення замовлення"

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1N3KMbEZXNr3sLmvpSnjbOYN',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="{}{}".format(settings.DOMAIN_NAME, reverse("orders:order_success")),
            cancel_url="{}{}".format(settings.DOMAIN_NAME, reverse("orders:order_canceled")),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)