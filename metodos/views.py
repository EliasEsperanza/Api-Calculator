# views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .hermite import hermite_interpolation
from .runge_kutta import runge_kutta
import numpy as np
from .models import CalculationHistory
from .serializers import CalculationHistorySerializer

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def hermite_view(request):
    x_values = request.data['x_values']
    y_values = request.data['y_values']
    derivatives = request.data['derivatives']
    z, q, steps, plot_x, plot_y = hermite_interpolation(x_values, y_values, derivatives)

    q_formatted = []
    for row in q:
        q_formatted.append({f"q{j}": value for j, value in enumerate(row)})

    response_data = {
        "Puntos de interpolacion (z)": z,
        "Tabla de diferencias divididas (q)": q_formatted,
        "plot_data": {
            "x": plot_x,
            "y": plot_y
        }
    }

    if request.user.is_authenticated:
        response_data["Pasos del calculo"] = steps

    return Response(response_data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def runge_kutta_view(request):
    try:
        y0 = float(request.data['initialValue'])
        x0 = float(request.data['startTime'])
        x_end = float(request.data['endTime'])
        h = float(request.data['stepSize'])
        function = request.data['function']
        
        def func(x, y):
            return eval(function, {"__builtins__": {}}, {'x': x, 'y': y})
        
        result, steps, plot_x, plot_y = runge_kutta(func, y0, x0, x_end, h)
        
        formatted_result = [{"x": x, "y": y} for x, y in result]
        
        response_data = {
            "result": formatted_result,
            "plot_data": {
                "x": plot_x,
                "y": plot_y
            }
        }

        if request.user.is_authenticated:
            response_data["steps"] = steps

        return Response(response_data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


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
