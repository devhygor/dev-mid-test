from django.shortcuts import render
from .controllers.calculos_controller import (
    CalculadoraController,
    NumerosPrimosController,
    FatorialController,
    PalindromoController,
    TabelaController,
    ContadorVogaisController,
    MediaNotasController,
    CalculoJurosController,
)

def calculadora(request):
    resultado = None
    error_message = None
    operacao = None

    if request.method == 'POST':
        numero1 = request.POST['numero1']
        numero2 = request.POST['numero2']
        operador = request.POST['operador']

        resultado, error_message = CalculadoraController().calcular(numero1, numero2, operador)
        operacao = f"{numero1} {operador} {numero2}"

    return render(request, 'calculadora.html', {
        'resultado': resultado,
        'error_message': error_message,
        'operacao': operacao})

def numeros_primos(request):
    primos = None
    numero_inicio = None
    if request.method == 'POST':
        numero_inicio = int(request.POST['numero_inicio'])
        primos = NumerosPrimosController().obter_10_primeiros_primos(numero_inicio)

    return render(request, 'numeros_primos.html', {'primos': primos, 'numero_inicio': numero_inicio})

def fatorial(request):
    resultado = None
    numero = None
    if request.method == 'POST':
        numero = int(request.POST['numero'])
        resultado = FatorialController().calcular_fatorial(numero)

    return render(request, 'fatorial.html', {'resultado': resultado, 'numero': numero})

def palindromo(request):
    resultado = None
    if request.method == 'POST':
        palavra = request.POST['palavra']
        resultado = PalindromoController().eh_palindromo(palavra)

    return render(request, 'palindromo.html', {'resultado': resultado})

def tabela(request):
    tabela = None
    numero = None
    if request.method == 'POST':
        numero = int(request.POST['numero'])
        tabela = TabelaController().gerar_tabela(numero)

    return render(request, 'tabela.html', {'tabela': tabela, 'numero': numero})

def contador_vogais(request):
    num_vogais = None
    if request.method == 'POST':
        frase = request.POST['frase']
        num_vogais = ContadorVogaisController().contar_vogais(frase)

    return render(request, 'contador_vogais.html', {'num_vogais': num_vogais})

def media_notas(request):
    media = None
    if request.method == 'POST':
        nota1 = float(request.POST['nota1'])
        nota2 = float(request.POST['nota2'])
        nota3 = float(request.POST['nota3'])
        media = MediaNotasController().calcular_media(nota1, nota2, nota3)

    return render(request, 'media_notas.html', {'media': media})

def calculo_juros(request):
    montante_final = None

    if request.method == 'POST':
        capital_inicial = float(request.POST['capital_inicial'])
        taxa_juros = float(request.POST['taxa_juros'])
        tempo_meses = int(request.POST['tempo_meses'])

        calculadora = CalculoJurosController()
        montante_final = calculadora.calcular_juros(capital_inicial, taxa_juros, tempo_meses)

    return render(request, 'calculo_juros.html', {'montante_final': montante_final})
