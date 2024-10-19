from django.urls import path, include

urlpatterns = [
    path('v1/', include('transfer_listener.api.v1.urls')),
]
