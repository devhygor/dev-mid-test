def calcular_model(numero1, numero2, operador):
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except ValueError:
        return None, "Por favor, insira números válidos."

    if operador == '+':
        resultado = numero1 + numero2
    elif operador == '-':
        resultado = numero1 - numero2
    elif operador == '*':
        resultado = numero1 * numero2
    elif operador == '/':
        if numero2 == 0:
            return None, "Erro: divisão por zero não é permitida."
        resultado = numero1 / numero2
    else:
        return None, "Operador inválido. Use +, -, * ou /."

    return resultado, None

def obter_10_primeiros_primos_model(numero_inicio):
    primos = []
    numero = numero_inicio
    while len(primos) < 10:
        if is_primo_model(numero):
            primos.append(numero)
        numero += 1
    return primos

def is_primo_model(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_fatorial_model(numero):
    if numero < 0:
        return "Erro: fatorial de número negativo não é definido."
    elif numero == 0 or numero == 1:
        return 1

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i
    return fatorial

def eh_palindromo_model(palavra):
    palavra = palavra.lower().replace(' ', '')
    return palavra == palavra[::-1]

def gerar_tabela_model(numero):
    tabela = []
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        tabela.append((multiplicador, numero, resultado))
    return tabela

def contar_vogais_model(frase):
    vogais = "aeiou"
    num_vogais = 0
    for letra in frase.lower():
        if letra in vogais:
            num_vogais += 1
    return num_vogais

def calcular_media_model(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def calcular_juros_model(capital_inicial, taxa_juros, tempo_meses):
    montante_final = capital_inicial * (1 + taxa_juros / 100) ** tempo_meses
    return montante_final
