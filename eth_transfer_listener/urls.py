from django.urls import path, include

urlpatterns = [
    path('api/', include('transfer_listener.api.urls')),
]
