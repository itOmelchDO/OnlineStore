from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSET

router = routers.DefaultRouter()
router.register(r"products", ProductModelViewSET)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "api"
