from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Sucursal
from .serializers import SucursalSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all().order_by("-id")
    serializer_class = SucursalSerializer

    @action(detail=False, methods=["get"])
    def activas(self, request):
        queryset = self.get_queryset().filter(status=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)