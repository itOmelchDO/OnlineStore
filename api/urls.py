from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSET, BasketModelViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductModelViewSET)
router.register(r"basket", BasketModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "api"
