from keras.models import load_model
from labs.design.models.usd import * 

from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from sklearn.preprocessing import MinMaxScaler

import numpy as np
import os
import random

class PredictViewsets(generics.CreateAPIView, viewsets.GenericViewSet):

    def sliding_window(self, data, window=7, step_size=1):
        X_test = []
        y_test = []
        for i in range(window, data.shape[0]):
            X_test.append(data[i-window:i])
            y_test.append(data[i])

        X_test, y_test = np.array(X_test), np.array(y_test)
        return X_test, y_test

    def validate(self, data):

        if 'histories' not in data:
            if type(data['histories']) is not type(list()):
                raise BaseException("Histories only array data")
            raise BaseException("Histories is required")
        elif 'model' not in data:
            raise BaseException("Model is required")

        elif 'range' not in data:
            if type(int(data['range'])) is not type(int()):
                assert BaseException("Range must integer")
            raise BaseException("Range is required")

        return data

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            validate = self.validate(data)
        except BaseException as e:
            return Response({'message': str(e)}, status=400)
        
        predicted = []
        for i in range(int(request.data['range'])):
            predicted.append({"time":i, "value": random.randint(800, 3000)})

        return Response(predicted, status=status.HTTP_200_OK)
        
        datatest = request.data['datatest']
        scaled = MinMaxScaler(feature_range=(-1, 1))
        
        datatest = np.array(datatest)
        datatest = datatest.reshape(len(datatest), 1)
        
        datatest_scaled = scaled.fit_transform(datatest)
        
        X_test, y_test = self.sliding_window(data=np.array(datatest_scaled), window=9, step_size=1)
        model = request.data['model']
        print(os.getcwd()) 
        if model == 'usd-idr':
            model_selected = os.path(
                f"{os.getcwd()}/labs/design/models/usd")
        else:
            model_selected = os.path(f"{os.getcwd()}/labs/design/models/jpy")

        return Response({
            'X_test': X_test.shape, 'y_test': y_test.shape, 'model': model_selected})

        model = request.data['model']
        model_selected = os.path(f'labs/design/models/usd/{model}')

        return Response({
                'model': model_selected,
                'dataset': datatest
            }, status=status.HTTP_200_OK)
