import joblib
import numpy as np
from pathlib import Path

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentPerformanceSerializer


# Load model safely using absolute path
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'model.pkl'
model = joblib.load(MODEL_PATH)


@api_view(['POST'])
def predict_performance(request):
    serializer = StudentPerformanceSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    validated_data = serializer.validated_data

    features = np.array([[
        validated_data['hours_studied'],
        validated_data['previous_scores'],
        1 if validated_data['extracurricular'] else 0,
        validated_data['sleep_hours'],
        validated_data['sample_papers'],
    ]])

    prediction = model.predict(features)[0]

    return Response({
        'predicted_performance_index': round(float(prediction), 2)
    })


def home(request):
    """Render the HTML prediction interface"""
    return render(request, 'predict.html')
