from django.urls import path

from .transfers.views import TransferView


urlpatterns = [
    path('transfers/', TransferView.as_view())
]
