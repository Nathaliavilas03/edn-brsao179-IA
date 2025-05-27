# Exercício 01 - Calculadora com tratamento de erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as ve:
        print(f"Erro: {ve}. Tente novamente.")
    except ZeroDivisionError as ze:
        print(f"Erro: {ze}. Tente novamente.")


# Exercício 02 - Registro de notas
notas = []

while True:
    entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")


# Exercício 03 - Verificação de senha forte
while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ")
    if senha.lower() == 'sair':
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte registrada.")
        break
    else:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres e conter ao menos um número.")


# Exercício 04 - Verificação de par ou ímpar
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: entrada inválida. Digite um número inteiro.")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
