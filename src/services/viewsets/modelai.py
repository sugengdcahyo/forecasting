from rest_framework import (
        generics, status, viewsets)
from rest_framework.response import Response

import os

class ModelViewsets(generics.ListAPIView, viewsets.GenericViewSet):

    def list(self, request, *args, **kwargs):
        models = ['usd-idr', 'jpy-idr']
        return Response({'models': models})
