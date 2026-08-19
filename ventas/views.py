from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ventas
from .serializers import VentasSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all().order_by("-id")
    serializer_class = VentasSerializer

    @action(detail=False, methods=["get"])
    def completadas(self, request):
        queryset = self.get_queryset().filter(estatus="Completada")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    





    