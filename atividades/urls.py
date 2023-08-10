from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora_view, name='calculadora'),
    path('calculadora/', views.calculadora_view, name='calculadora'),
    path('numeros_primos/', views.numeros_primos_view, name='numeros_primos'),
    path('fatorial/', views.fatorial_view, name='fatorial'),
    path('palindromo/', views.palindromo_view, name='palindromo'),
    path('tabela/', views.tabela_view, name='tabela'),
    path('contador_vogais/', views.contador_vogais_view, name='contador_vogais'),
    path('media_notas/', views.media_notas_view, name='media_notas'),
    path('calculo_juros/', views.calculo_juros_view, name='calculo_juros'),
]
