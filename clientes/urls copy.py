from django.urls import path
from .views import ClienteListCreateAPIView, ClienteUpdateDeleteAPIView

urlpatterns = [
    path('clientes/', ClienteListCreateAPIView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteUpdateDeleteAPIView.as_view(), name='cliente-update-delete'),
]