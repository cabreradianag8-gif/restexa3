from rest_framework import serializers
from .models import Ventas
from productos.serializers import ProductoSerializer
from inventarios.serializers import InventarioSerializer

class VentasSerializer(serializers.ModelSerializer):
    producto_info = ProductoSerializer(source='producto', read_only=True)
    inventario_info = InventarioSerializer(source='inventario', read_only=True)

    class Meta:
        model = Ventas
        fields = '__all__'