from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tema/<int:id>/', views.detalle_tema, name='detalle_tema'),
]