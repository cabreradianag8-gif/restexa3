from django.urls import path
from .views import (
    VentasListCreateAPIView, VentasUpdateDeleteAPIView,
    DetalleVentaListCreateAPIView, DetalleVentaUpdateDeleteAPIView
)

urlpatterns = [
    path('ventas/', VentasListCreateAPIView.as_view(), name='ventas-list-create'),
    path('ventas/<int:pk>/', VentasUpdateDeleteAPIView.as_view(), name='ventas-update-delete'),
    path('detalles-venta/', DetalleVentaListCreateAPIView.as_view(), name='detalleventa-list-create'),
    path('detalles-venta/<int:pk>/', DetalleVentaUpdateDeleteAPIView.as_view(), name='detalleventa-update-delete'),
]