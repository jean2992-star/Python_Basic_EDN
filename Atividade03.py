# Classificador de Idade
idade = int(input("Digite a sua idade: "))
    
if 0 <= idade <= 12:
        print("Categoria: Criança")
elif 13 <= idade <= 17:
        print("Categoria: Adolescente")
elif 18 <= idade <= 59:
        print("Categoria: Adulto")
else:
        print("Categoria: Idoso")

# Calculadora de IMC
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
    
imc = peso / (altura ** 2)
    
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
        
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

 
# Conversor de Temperatura
temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
unidade_destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
    
if unidade_origem == 'C':
    if unidade_destino == 'F':
            resultado = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
            resultado = temperatura + 273.15
    else:
            resultado = temperatura
elif unidade_origem == 'F':
    if unidade_destino == 'C':
            resultado = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
            resultado = (temperatura - 32) * 5/9 + 273.15
    else:
            resultado = temperatura
elif unidade_origem == 'K':
    if unidade_destino == 'C':
            resultado = temperatura - 273.15
    elif unidade_destino == 'F':
            resultado = (temperatura - 273.15) * 9/5 + 32
    else:
            resultado = temperatura
else:
    print("Unidade de origem inválida")
     
print(f"{temperatura} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")


# Verificador de Ano Bissexto
ano = int(input("Digite um ano: "))
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
else:
        print(f"{ano} não é um ano bissexto.")

