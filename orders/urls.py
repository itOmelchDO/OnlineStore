from django.urls import path

from orders.views import OrderCreateView

urlpatterns = [
    path("order-create/", OrderCreateView.as_view(), name="order_create"),
]

app_name = "orders"
