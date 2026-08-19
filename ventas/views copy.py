from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ventas, DetalleVenta
from .serializers import VentasSerializer, DetalleVentaSerializer

class VentasListCreateAPIView(APIView):
    def get(self, request):
        query_set = Ventas.objects.all().order_by("-id")
        serializar = VentasSerializer(query_set, many=True)
        return Response(serializar.data)

    def post(self, request):
        serializer = VentasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VentasUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Ventas, pk=pk)

    def get(self, request, pk):
        venta = self.get_object(pk)
        serializer = VentasSerializer(venta)
        return Response(serializer.data)

    def put(self, request, pk):
        venta = self.get_object(pk)
        serializer = VentasSerializer(venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        venta = self.get_object(pk)
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetalleVentaListCreateAPIView(APIView):
    def get(self, request):
        query_set = DetalleVenta.objects.all().order_by("-id")
        serializar = DetalleVentaSerializer(query_set, many=True)
        return Response(serializar.data)

    def post(self, request):
        serializer = DetalleVentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleVentaUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(DetalleVenta, pk=pk)

    def get(self, request, pk):
        detalle = self.get_object(pk)
        serializer = DetalleVentaSerializer(detalle)
        return Response(serializer.data)

    def put(self, request, pk):
        detalle = self.get_object(pk)
        serializer = DetalleVentaSerializer(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        detalle = self.get_object(pk)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)