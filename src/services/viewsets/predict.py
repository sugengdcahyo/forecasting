from rest_framework import generics, status
from rest_framework.response import Response

class PredictViewsets(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        return Response({
            "data": "predicted."
        }, status=status.HTTP_200_OK)