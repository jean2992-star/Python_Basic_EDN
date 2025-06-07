import csv
import os

def ler_e_exibir_csv(nome_arquivo='pessoas.csv'):
   
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
        print("Por favor, certifique-se de que o arquivo esteja no mesmo diretório do script")
        print("ou forneça o caminho completo para o arquivo.")
        return

    try:
        # Abre o arquivo CSV em modo de leitura ('r').
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)

            print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")

            # Itera sobre cada linha no arquivo CSV
            for linha in leitor_csv:
                print(linha)

    except IOError as e:
        print(f"Erro de I/O ao tentar ler o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Chamada da função para ler e exibir o arquivo CSV ---
if __name__ == "__main__":
    nome_do_arquivo = 'pessoas.csv'

    ler_e_exibir_csv(nome_do_arquivo)