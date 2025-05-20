def calculadora():
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
                # Tratamento de divisão por zero
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                # Operação inválida
                print("Operação inválida! Use apenas +, -, * ou /.")
                continue

            print(f"Resultado: {resultado}")
            break  # Sai do loop após operação bem sucedida

        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")

calculadora()


def registro_notas():
    notas = []
    while True:
        entrada = input("Digite uma nota de 0 a 10 ou 'fim' para encerrar: ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite uma nota numérica ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

registro_notas()



def senha_forte():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            print("Encerrando programa.")
            break

        # Verifica tamanho e presença de números
        tem_numero = any(char.isdigit() for char in senha)
        if len(senha) >= 8 and tem_numero:
            print("Senha válida e forte!")
            break
        else:
            print("Senha fraca! Deve ter pelo menos 8 caracteres e conter pelo menos um número.")

senha_forte()



def par_ou_impar():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            num = int(entrada)
            if num % 2 == 0:
                print(f"{num} é par.")
                pares += 1
            else:
                print(f"{num} é ímpar.")
                impares += 1
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

par_ou_impar()
