from atividades.models import calcular_model, is_primo_model, obter_10_primeiros_primos_model, \
    calcular_fatorial_model, eh_palindromo_model, gerar_tabela_model, contar_vogais_model, \
    calcular_media_model, calcular_juros_model

class CalculadoraController:
    def calcular_controller(self, numero1, numero2, operador):
        return calcular_model(numero1, numero2, operador)

class NumerosPrimosController:
    def is_primo_controller(self, numero_inicio):
        return is_primo_model(numero_inicio)

    def obter_10_primeiros_primos_controller(self, numero_inicio):
        return obter_10_primeiros_primos_model(numero_inicio)

class FatorialController:
    def calcular_fatorial_controller(self, numero):
        return calcular_fatorial_model(numero)

class PalindromoController:
    def eh_palindromo_controller(self, palavra):
        return eh_palindromo_model(palavra)

class TabelaController:
    def gerar_tabela_controller(self, numero):
        return gerar_tabela_model(numero)

class ContadorVogaisController:
    def contar_vogais_controller(self, frase):
        return contar_vogais_model(frase)

class MediaNotasController:
    def calcular_media_controller(self, nota1, nota2, nota3):
        return calcular_media_model(nota1, nota2, nota3)

class CalculoJurosController:
    def calcular_juros_controller(self, capital_inicial, taxa_juros, tempo_meses):
        montante_final = calcular_juros_model(capital_inicial, taxa_juros, tempo_meses)
        return montante_final
