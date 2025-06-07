import csv

def escrever_dados_pessoas_csv(nome_arquivo='pessoas.csv'):
    
    # Defina os dados  
    dados_pessoas = [
        ['Nome', 'Idade', 'Cidade'],  # Cabeçalho
        ['Alice', 30, 'São Paulo'],
        ['Bob', 24, 'Rio de Janeiro'],
        ['Carlos', 35, 'Belo Horizonte'],
        ['Diana', 28, 'Curitiba'],
        ['Eduardo', 42, 'Porto Alegre']
    ]

    try:
        # Abre o arquivo CSV em modo de escrita ('w').
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)

            # Escreve todas as linhas de uma vez.
            escritor_csv.writerows(dados_pessoas)

        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        print("Conteúdo:")
        # Ler e imprimir o conteúdo  
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            print(arquivo_csv.read())

    except IOError as e:
        print(f"Erro de I/O ao tentar escrever o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Chamada da função para criar o arquivo CSV ---
if __name__ == "__main__":            
    escrever_dados_pessoas_csv('minhas_pessoas.csv')
