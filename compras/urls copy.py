from django.urls import path
from .views import (
    ComprasListCreateAPIView, ComprasUpdateDeleteAPIView,
    DetalleCompraListCreateAPIView, DetalleCompraUpdateDeleteAPIView
)

urlpatterns = [
    path('compras/', ComprasListCreateAPIView.as_view(), name='compras-list-create'),
    path('compras/<int:pk>/', ComprasUpdateDeleteAPIView.as_view(), name='compras-update-delete'),
    path('detalles-compra/', DetalleCompraListCreateAPIView.as_view(), name='detallecompra-list-create'),
    path('detalles-compra/<int:pk>/', DetalleCompraUpdateDeleteAPIView.as_view(), name='detallecompra-update-delete'),
]