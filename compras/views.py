from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Compras
from .serializers import ComprasSerializer

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all().order_by("-id")
    serializer_class = ComprasSerializer

    @action(detail=False, methods=["get"])
    def procesadas(self, request):
        queryset = self.get_queryset().filter(estatus="Procesada")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)