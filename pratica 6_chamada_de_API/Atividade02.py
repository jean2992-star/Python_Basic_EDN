import requests

def gerar_perfil_usuario():
    """Gera um perfil de usuário aleatório usando a API Random User Generator."""
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        dados_usuario = response.json()

        if dados_usuario and "results" in dados_usuario and len(dados_usuario["results"]) > 0:
            usuario = dados_usuario["results"][0]
            nome_completo = f"{usuario['name']['title']} {usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("\n--- Perfil de Usuário Gerado ---")
            print(f"Nome: {nome_completo}")
            print(f"Email: {email}")
            print(f"País: {pais}")
        else:
            print("Não foi possível obter dados do usuário.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
    except (KeyError, IndexError):
        print("Erro ao processar os dados recebidos da API. O formato pode ter mudado.")

if __name__ == "__main__":
    gerar_perfil_usuario()