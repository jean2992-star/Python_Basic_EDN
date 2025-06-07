import random
import string

def gerar_senha(comprimento):
    """Gera uma senha aleatória com o comprimento especificado."""
    if comprimento < 4:
        print("O comprimento da senha deve ser de pelo menos 4 caracteres para incluir todos os tipos de caracteres.")
        return None

    # Define os caracteres a serem usados
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    # Garante pelo menos um de cada tipo
    senha_parcial = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    # Completa o restante da senha com uma combinação de todos os caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    senha_restante = [random.choice(todos_caracteres) for _ in range(comprimento - 4)]

    senha_lista = senha_parcial + senha_restante
    random.shuffle(senha_lista)  # Embaralha para garantir aleatoriedade na ordem

    return "".join(senha_lista)

if __name__ == "__main__":
    try:
        num_caracteres = int(input("Digite a quantidade de caracteres para a senha: "))
        senha_gerada = gerar_senha(num_caracteres)
        if senha_gerada:
            print("Senha gerada:", senha_gerada)
    except ValueError:
        print("Por favor, insira um número válido para o comprimento da senha.")