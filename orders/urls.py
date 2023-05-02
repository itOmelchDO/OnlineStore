from django.urls import path

from orders.views import OrderCreateView, SuccessTemplateView, CanceledTemplateView

urlpatterns = [
    path("order-create/", OrderCreateView.as_view(), name="order_create"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order-canceled/", SuccessTemplateView.as_view(), name="order_canceled"),
]

app_name = "orders"
