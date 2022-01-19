from django.urls import path, include
from services.viewsets.predict import PredictViewsets
from services.viewsets import modelai
from rest_framework import routers

router = routers.DefaultRouter()

router.register('models', modelai.ModelViewsets, basename='models-viewsets')
router.register('predict', PredictViewsets, basename='predict-viewsets')

service_urls = router.urls
