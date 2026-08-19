from django.urls import path
from .views import InventarioListCreateAPIView, InventarioUpdateDeleteAPIView

urlpatterns = [
    path('inventarios/', InventarioListCreateAPIView.as_view(), name='inventario-list-create'),
    path('inventarios/<int:pk>/', InventarioUpdateDeleteAPIView.as_view(), name='inventario-update-delete'),
]