from django.urls import path
from . import views

urlpatterns = [
    path('hermite/', views.hermite_view),
    path('runge_kutta/', views.runge_kutta_view),
    path('save_history/', views.save_history),
    path('get_history/', views.get_history),
]
