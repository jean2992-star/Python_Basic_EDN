def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso
valor = 150.00
percent = 15
print(f"Gorjeta para conta de R${valor:.2f} com {percent}%: R${calcular_gorjeta(valor, percent):.2f}")



import string

def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Retorna "Sim" se for palíndromo, "Não" caso contrário.
    """
    # Remove espaços, pontuação e deixa tudo em minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    # Verifica se texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplos:
print(eh_palindromo("A man, a plan, a canal: Panama"))  # Deve retornar "Sim"
print(eh_palindromo("Python"))                         # Deve retornar "Não"


def senha_forte():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            print("Encerrando programa.")
            break

        tem_numero = any(char.isdigit() for char in senha)
        if len(senha) >= 8 and tem_numero:
            print("Senha válida e forte!")
            break
        else:
            print("Senha fraca! Deve ter pelo menos 8 caracteres e conter pelo menos um número.")

# Para rodar o programa:
senha_forte()



from datetime import date

def idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade da pessoa em dias baseado no ano de nascimento até a data atual.

    Parâmetros:
    ano_nascimento (int): Ano de nascimento da pessoa

    Retorna:
    int: Idade aproximada em dias
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação simples, não considera anos bissextos
    return idade_dias

# Exemplo:
ano = 1990
print(f"Idade aproximada em dias para quem nasceu em {ano}: {idade_em_dias(ano)} dias")
