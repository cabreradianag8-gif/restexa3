from django.urls import path
from .views import SucursalListCreateAPIView, SucursalUpdateDeleteAPIView

urlpatterns = [
    path('sucursales/', SucursalListCreateAPIView.as_view(), name='sucursal-list-create'),
    path('sucursales/<int:pk>/', SucursalUpdateDeleteAPIView.as_view(), name='sucursal-update-delete'),
]