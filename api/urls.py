from django.urls import include, path
from rest_framework import routers

from api.views import BasketModelViewSet, ProductModelViewSET

router = routers.DefaultRouter()
router.register(r"products", ProductModelViewSET)
router.register(r"baskets", BasketModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "api"
