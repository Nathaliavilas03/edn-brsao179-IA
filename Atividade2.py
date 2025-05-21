"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""


valor_reais = 100.00
tx_dolar = 5.20
tx_euro = 6.15

calculo_dolar = valor_reais / tx_dolar
calculo_euro = valor_reais / tx_euro

print(f"Valor em reais: {valor_reais} \nValor em dólar: {calculo_dolar:.2f} \nValor em euro: {calculo_euro:.2f}")


"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

camiseta = 50.00
desconto = 0.2

cal_desconto = camiseta - (camiseta * desconto)

print(f"Valor original da camiseta: {camiseta} reais \nvalor da camiseta com desconto de 20% é de: {cal_desconto} reais")

"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, 
arredondando para duas casas decimais."""

n1= 7.5
n2= 8.0
n3= 6.5

media = (n1 + n2 + n3) / 3 

print("Nota 1 = 7.5 \nNota 2 = 8.0 \nNota 3 = 6.5 ")
print(f"A média do aluno é de: {media:.2f}")

"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
incluindo o resultado final arredondado para duas casas decimais."""

distancia = 300
combustivel_gasto = 25

consumo_medio = distancia / combustivel_gasto

print("=== Relatório da Viagem ===")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")