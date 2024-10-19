from rest_framework.generics import ListAPIView

from transfer_listener.models import Transfer

from .serializers import TransferSerializer
from .filters import TransferFilter


class TransferView(ListAPIView):
    queryset = Transfer.objects.order_by('-block_number')
    serializer_class = TransferSerializer
    filterset_class = TransferFilter
