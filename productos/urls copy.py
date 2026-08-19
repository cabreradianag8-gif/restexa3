from django.urls import path
from .views import ProductoListCreateAPIView, ProductoUpdateDeleteAPIView

urlpatterns = [
    path('productos/', ProductoListCreateAPIView.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoUpdateDeleteAPIView.as_view(), name='producto-update-delete'),
]