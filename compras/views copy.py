from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Compras, DetalleCompra
from .serializers import ComprasSerializer, DetalleCompraSerializer

class ComprasListCreateAPIView(APIView):
    def get(self, request):
        query_set = Compras.objects.all().order_by("-id")
        serializar = ComprasSerializer(query_set, many=True)
        return Response(serializar.data)

    def post(self, request):
        serializer = ComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComprasUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Compras, pk=pk)

    def get(self, request, pk):
        compra = self.get_object(pk)
        serializer = ComprasSerializer(compra)
        return Response(serializer.data)

    def put(self, request, pk):
        compra = self.get_object(pk)
        serializer = ComprasSerializer(compra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        compra = self.get_object(pk)
        compra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetalleCompraListCreateAPIView(APIView):
    def get(self, request):
        query_set = DetalleCompra.objects.all().order_by("-id")
        serializar = DetalleCompraSerializer(query_set, many=True)
        return Response(serializar.data)

    def post(self, request):
        serializer = DetalleCompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleCompraUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(DetalleCompra, pk=pk)

    def get(self, request, pk):
        detalle = self.get_object(pk)
        serializer = DetalleCompraSerializer(detalle)
        return Response(serializer.data)

    def put(self, request, pk):
        detalle = self.get_object(pk)
        serializer = DetalleCompraSerializer(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        detalle = self.get_object(pk)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)