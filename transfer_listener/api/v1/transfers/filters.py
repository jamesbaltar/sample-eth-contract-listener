from django_filters import rest_framework as filters

from transfer_listener.models import Transfer


class TransferFilter(filters.FilterSet):
    token_id = filters.NumberFilter(field_name="token_id")

    class Meta:
        model = Transfer
        fields = ['token_id']
