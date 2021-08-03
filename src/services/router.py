from django.urls import path, include
from services.viewsets.predict import PredictViewsets
service_urls = [
    path('predict/', PredictViewsets.as_view(), name='models_routers'),
]