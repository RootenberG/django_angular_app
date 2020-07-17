from .models import BalanceSheet
from rest_framework import viewsets
from .serializers import BalanceSheetSerializer


class BalanceSheetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """

    queryset = BalanceSheet.objects.all()
    serializer_class = BalanceSheetSerializer
