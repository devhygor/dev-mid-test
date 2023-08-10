import json
from django.http import JsonResponse
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

def calculadora_view(request):
    resultado = None
    error_message = None
    operacao = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            numero1 = data.get('numero1')
            numero2 = data.get('numero2')
            operador = data.get('operador')

            if numero1 is not None and numero2 is not None and operador is not None:
                resultado, error_message = CalculadoraController().calcular_controller(numero1, numero2, operador)
                return JsonResponse({'resultado': resultado, 'error_message': error_message})

        else:  # Process HTML form data
            numero1 = request.POST.get('numero1')
            numero2 = request.POST.get('numero2')
            operador = request.POST.get('operador')

            if numero1 is not None and numero2 is not None and operador is not None:
                resultado, error_message = CalculadoraController().calcular_controller(numero1, numero2, operador)
                operacao = f"{numero1} {operador} {numero2}"

    return render(request, 'calculadora.html', {
        'resultado': resultado,
        'error_message': error_message,
        'operacao': operacao
    })

def numeros_primos_view(request):
    numeros_primos = None
    numero_inicio = None
    is_numero_primo = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            numero_inicio = data.get('numero_inicio')

            if numero_inicio is not None:
                is_numero_primo = NumerosPrimosController().is_primo_controller(numero_inicio)
                numeros_primos = NumerosPrimosController().obter_10_primeiros_primos_controller(numero_inicio)
                return JsonResponse({'numeros_primos': numeros_primos,
                                     'is_numero_primo': is_numero_primo})

        else:  # Process HTML form data
            numero_inicio = int(request.POST.get('numero_inicio'))

            if numero_inicio is not None:
                is_numero_primo = NumerosPrimosController().is_primo_controller(numero_inicio)
                numeros_primos = NumerosPrimosController().obter_10_primeiros_primos_controller(numero_inicio)

    return render(request, 'numeros_primos.html', {
        'numeros_primos': numeros_primos,
        'numero_inicio': numero_inicio,
        'is_numero_primo': is_numero_primo
    })

def fatorial_view(request):
    resultado = None
    numero = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            numero = data.get('numero')

            if numero is not None:
                resultado = FatorialController().calcular_fatorial_controller(numero)
                return JsonResponse({'resultado': resultado})

        else:  # Process HTML form data
            numero = int(request.POST.get('numero'))

            if numero is not None:
                resultado = FatorialController().calcular_fatorial_controller(numero)

    return render(request, 'fatorial.html', {'resultado': resultado, 'numero': numero})

def palindromo_view(request):
    resultado = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            palavra = data.get('palavra')

            if palavra is not None:
                resultado = PalindromoController().eh_palindromo_controller(palavra)
                return JsonResponse({'resultado': resultado})

        else:  # Process HTML form data
            palavra = request.POST.get('palavra')

            if palavra is not None:
                resultado = PalindromoController().eh_palindromo_controller(palavra)

    return render(request, 'palindromo.html', {'resultado': resultado})

def tabela_view(request):
    tabela = None
    numero = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            numero = data.get('numero')

            if numero is not None:
                tabela = TabelaController().gerar_tabela_controller(numero)
                return JsonResponse({'tabela': tabela})

        else:  # Process HTML form data
            numero = int(request.POST.get('numero'))

            if numero is not None:
                tabela = TabelaController().gerar_tabela_controller(numero)

    return render(request, 'tabela.html', {'tabela': tabela, 'numero': numero})

def contador_vogais_view(request):
    num_vogais = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            frase = data.get('frase')

            if frase is not None:
                num_vogais = ContadorVogaisController().contar_vogais_controller(frase)
                return JsonResponse({'num_vogais': num_vogais})

        else:  # Process HTML form data
            frase = request.POST.get('frase')

            if frase is not None:
                num_vogais = ContadorVogaisController().contar_vogais_controller(frase)

    return render(request, 'contador_vogais.html', {'num_vogais': num_vogais})

def media_notas_view(request):
    media = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            nota1 = data.get('nota1')
            nota2 = data.get('nota2')
            nota3 = data.get('nota3')

            if nota1 is not None and nota2 is not None and nota3 is not None:
                media = MediaNotasController().calcular_media_controller(nota1, nota2, nota3)
                return JsonResponse({'media': media})

        else:  # Process HTML form data
            nota1 = float(request.POST.get('nota1'))
            nota2 = float(request.POST.get('nota2'))
            nota3 = float(request.POST.get('nota3'))

            if nota1 is not None and nota2 is not None and nota3 is not None:
                media = MediaNotasController().calcular_media_controller(nota1, nota2, nota3)

    return render(request, 'media_notas.html', {'media': media})

def calculo_juros_view(request):
    montante_final = None

    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            capital_inicial = data.get('capital_inicial')
            taxa_juros = data.get('taxa_juros')
            tempo_meses = data.get('tempo_meses')

            if capital_inicial is not None and taxa_juros is not None and tempo_meses is not None:
                calculadora = CalculoJurosController()
                montante_final = calculadora.calcular_juros_controller(capital_inicial, taxa_juros, tempo_meses)
                return JsonResponse({'montante_final': montante_final})

        else:  # Process HTML form data
            capital_inicial = float(request.POST.get('capital_inicial'))
            taxa_juros = float(request.POST.get('taxa_juros'))
            tempo_meses = int(request.POST.get('tempo_meses'))

            if capital_inicial is not None and taxa_juros is not None and tempo_meses is not None:
                calculadora = CalculoJurosController()
                montante_final = calculadora.calcular_juros_controller(capital_inicial, taxa_juros, tempo_meses)

    return render(request, 'calculo_juros.html', {'montante_final': montante_final})
