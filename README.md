# TEST MID LEVEL

## Descrição

    Atividades desenvolvidas para suprir com as necessidades repassadas para o teste dev-mid-test repassadas pelo Roman

    Fiz uma forma em que da tanto para testar pelo postman, insominia etc... como que se fosse uma api, como acessando também a interface web diretamente, pela mesma url

## Pré Requisitos
* Tenha o python3 instalado, de preferencia na versão >= 3.11
* É aconselhável também que use uma virtual env para rodar o projeto, mas fica ao criterio de cada um.

## Instalaçao

  Para rodar o projeto na sua maquina com todos os pacotes necessarios basta executar os seguintes comandos no terminal:
  ```sh
    pip install -r requirements.txt
  ```

  E por fim execute o comando para iniciar o nosso servidor local:
  ```sh
    python manage.py runserver
  ```
  o projero ira rodar na porta 8000
  ```sh
    http://127.0.0.1:8000/
  ```

## Rotas
As rotas e os parametro direto para as atividades são:

### Calculadora
```sh
    http://127.0.0.1:8000/calculadora/
```

```json
{
    "numero1": 5,
    "operador": "+",
    "numero2": 8.5
}
```
### Números primos
```sh
    http://127.0.0.1:8000/numeros_primos/
```

```json
{
    "numero_inicio": 10
}
```
### Fatorial
```sh
    http://127.0.0.1:8000/fatorial/
```

```json
{
    "numero": 5
}
```
### Palindromo
```sh
    http://127.0.0.1:8000/palindromo/
```
```json
{
    "palavra": "teste"
}
```
### Tabela
```sh
    http://127.0.0.1:8000/tabela/
```
```json
{
    "numero": 5
}
```
### Contador de Vogais
```sh
    http://127.0.0.1:8000/contador_vogais/
```
```json
{
    "frase": "frase de teste"
}
```
### Média das Notas
```sh
    http://127.0.0.1:8000/media_notas/
```
```json
{
    "nota1": 5,
    "nota2": 10,
    "nota3": 8.5
}
```
### Calculo de juros
```sh
    http://127.0.0.1:8000/calculo_juros/
```
```json
{
    "capital_inicial": 5,
    "taxa_juros": 1,
    "tempo_meses": 2
}
```

    OBS: As rotas são tanto para o parametro GET e POST:

    GET ira retornar a pagina para preenchermos os valores
    POST para enviar os dados e retornar com o resultado

## Observação Importante

Se for testar diretamente pelo POSTMAN, INSOMNIA ou outra ferramente do tipo, precisamos acrescentar uma variavel no header do POST, com a seguinte ``KEY``: `X-CSRFToken` e para pegar o ``VALUE`` dessa KEY, podemos antes de fazer o post fazer um GET na url e pegarmos o valor q ira retornar no ``cookie``, que ai sim conseguiremos realizer um POST para o nosso projeto, exemplo de como deve ficar a nova variavel no header:

```sh
    X-CSRFToken : nhXGkAY93i3EUo8MaGOwbCukg6xWydrk
```

## Apresentação
 Fiz um pequeno video e postei no youtube, para apresentar o projeto com as atividades, na tentativa de facilitar a vida de quem for havaliar o projeto. https://youtu.be/ndSGujUT4Ek
