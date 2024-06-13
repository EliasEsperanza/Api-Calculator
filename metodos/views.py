# views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .hermite import hermite_interpolation
from .runge_kutta import runge_kutta
import numpy as np
from .models import CalculationHistory
from .serializers import CalculationHistorySerializer

@api_view(['POST'])
def hermite_view(request):
    x_values = request.data['x_values']
    y_values = request.data['y_values']
    derivatives = request.data['derivatives']
    z, q = hermite_interpolation(x_values, y_values, derivatives)
    return Response({"z": z, "q": q})

@api_view(['POST'])
def runge_kutta_view(request):
    def func(x, y):
        return eval(request.data['function'])
    y0 = request.data['initialValue']
    x0 = request.data['startTime']
    x_end = request.data['endTime']
    h = request.data['stepSize']
    result = runge_kutta(func, y0, x0, x_end, h)
    return Response({"result": result})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_history(request):
    method = request.data['method']
    input_data = request.data['input_data']
    result = request.data['result']
    CalculationHistory.objects.create(user=request.user, method=method, input_data=input_data, result=result)
    return Response(status=201)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_history(request):
    history = CalculationHistory.objects.filter(user=request.user)
    serializer = CalculationHistorySerializer(history, many=True)
    return Response(serializer.data)
