#Crie um programa que converta um valor em reais para dólares e euros.
Valor = 100.00
taxaDolar = 5.20
taxaEuro = 6.15
ValorDolar = Valor / taxaDolar
ValorEuro = Valor / taxaEuro

print("\nValor em Reais: R$", Valor)
print("Valor em Dólar: ", round(ValorDolar, 2))
print("Valor em Euro: ", round(ValorEuro, 2))

#Calculadora de Desconto

produto = "Camiseta"
preco = 50.00
porcentagem = 20
desconto = (preco * porcentagem) / 100
precoComDesconto = preco - desconto

print("\nProduto: ", produto)
print("Preço original: R$", preco)
print("Porcentagem: ", porcentagem, "%")   
print("Desconto: R$", round(desconto, 2))   
print("Preço com desconto: R$", round(precoComDesconto, 2)) 

#Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3
print("\nNotas: ", nota1, nota2, nota3)
print("Média: ", round(media, 2))

# Calculadora de Consumo de Combustível
distancia = 300  # em km
combustivel = 25 # em litros 
consumo = distancia / combustivel # em km/l
print("\nDistância: ", distancia, "km")
print("Combustível: ", combustivel, "litros")
print("Consumo médio: ", round(consumo, 2), "km/l")