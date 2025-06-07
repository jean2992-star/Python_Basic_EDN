import requests

def consultar_cep(cep):
    """Consulta informações de endereço a partir de um CEP usando a API ViaCEP."""
    cep_formatado = cep.replace("-", "").replace(".", "").strip()
    if not cep_formatado.isdigit() or len(cep_formatado) != 8:
        print("CEP inválido. Por favor, insira um CEP com 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados_endereco = response.json()

        if "erro" not in dados_endereco:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {dados_endereco.get('cep', 'N/A')}")
            print(f"Logradouro: {dados_endereco.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados_endereco.get('bairro', 'N/A')}")
            print(f"Cidade: {dados_endereco.get('localidade', 'N/A')}")
            print(f"Estado: {dados_endereco.get('uf', 'N/A')}")
        else:
            print(f"CEP {cep} não encontrado ou inválido.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API ViaCEP: {e}")
    except ValueError: # requests.json() pode levantar ValueError se a resposta não for JSON
        print("Erro ao decodificar a resposta da API. Não é um JSON válido.")


if __name__ == "__main__":
    cep_usuario = input("Digite o CEP para consulta (ex: 01001-000 ou 01001000): ")
    consultar_cep(cep_usuario) 