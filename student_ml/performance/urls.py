from django.urls import path
from .views import predict_performance, home

urlpatterns = [
    path('predict/', predict_performance),
    path('', home, name='home'),
]
