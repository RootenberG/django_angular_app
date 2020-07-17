from django.urls import path, include
from rest_framework import routers
from .views import BalanceSheetViewSet


router = routers.SimpleRouter()
router.register(r"", BalanceSheetViewSet)

urlpatterns = router.urls
