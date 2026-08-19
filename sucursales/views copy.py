from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Sucursal
from .serializers import SucursalSerializer

class SucursalListCreateAPIView(APIView):
    def get(self, request):
        query_set = Sucursal.objects.all().order_by("-id")
        serializar = SucursalSerializer(query_set, many=True)
        return Response(serializar.data)

    def post(self, request):
        serializer = SucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SucursalUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Sucursal, pk=pk)

    def get(self, request, pk):
        sucursal = self.get_object(pk)
        serializer = SucursalSerializer(sucursal)
        return Response(serializer.data)

    def put(self, request, pk):
        sucursal = self.get_object(pk)
        serializer = SucursalSerializer(sucursal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sucursal = self.get_object(pk)
        sucursal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)