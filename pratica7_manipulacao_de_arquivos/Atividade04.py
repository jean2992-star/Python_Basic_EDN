import json
import os

def escrever_dados_json(nome_arquivo='pessoa.json', dados_pessoa=None):

    if dados_pessoa is None:
        dados_pessoa = {
            'nome': 'João Silva',
            'idade': 29,
            'cidade': 'Chapecó'
        }

    try:
        # Abre o arquivo JSON em modo de escrita ('w').

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)
        print(f"Dados da pessoa foram escritos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro de I/O ao tentar escrever o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao escrever o arquivo: {e}")

def ler_dados_json(nome_arquivo='pessoa.json'):
   
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Por favor, execute a função 'escrever_dados_json' primeiro para criar o arquivo.")
        return None

    try:
        # Abre o arquivo JSON em modo de leitura ('r').
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        print(f"\nDados lidos de '{nome_arquivo}':")
        print(f"Nome: {dados.get('nome', 'N/A')}")
        print(f"Idade: {dados.get('idade', 'N/A')}")
        print(f"Cidade: {dados.get('cidade', 'N/A')}")
        return dados
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON do arquivo '{nome_arquivo}': {e}")
        print("Verifique se o arquivo JSON está formatado corretamente.")
        return None
    except IOError as e:
        print(f"Erro de I/O ao tentar ler o arquivo '{nome_arquivo}': {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

# --- Parte principal do programa ---
if __name__ == "__main__":
    nome_do_arquivo_json = 'minha_pessoa.json'

    print("--- Escrevendo dados no arquivo JSON ---")
    
    
    escrever_dados_json(nome_do_arquivo_json)

    nova_pessoa = {
          'nome': 'Maria Oliveira',
          'idade': 32,
          'cidade': 'São Paulo'
    }
    
    escrever_dados_json(nome_do_arquivo_json, nova_pessoa)

    print("\n--- Lendo dados do arquivo JSON ---")
    dados_carregados = ler_dados_json(nome_do_arquivo_json)

    # Você pode trabalhar com os dados carregados:
    if dados_carregados:
        print("\nTipo dos dados carregados:", type(dados_carregados))
        print("Acessando um campo específico:", dados_carregados['nome'])