from django.urls import path

from api.views import ProductListAPIView

urlpatterns = [
    path("product-list/", ProductListAPIView.as_view(), name="product_list"),
]

app_name = "api"
