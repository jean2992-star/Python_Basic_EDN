import requests
from datetime import datetime

def consultar_cotacao(codigo_moeda):
    """Consulta a cotação de uma moeda em relação ao BRL usando a AwesomeAPI."""
    codigo_moeda_upper = codigo_moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda_upper}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados_cotacao = response.json()

        # A API retorna um dicionário onde a chave é a combinação das moedas (ex: USDBRL)
        chave_api = f"{codigo_moeda_upper}BRL"
        if chave_api in dados_cotacao:
            cotacao = dados_cotacao[chave_api]
            nome = cotacao.get('name', 'N/A')
            valor_atual = float(cotacao.get('bid', '0'))
            maximo = float(cotacao.get('high', '0'))
            minimo = float(cotacao.get('low', '0'))
            timestamp_str = cotacao.get('create_date', None) # 'create_date' é mais confiável que 'timestamp'

            if timestamp_str:
                # Convertendo para um formato mais legível
                # Exemplo de formato de 'create_date': "2023-10-27 18:59:59"
                data_hora_atualizacao = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                data_hora_formatada = data_hora_atualizacao.strftime('%d/%m/%Y %H:%M:%S')
            else:
                data_hora_formatada = "N/A"


            print(f"\n--- Cotação {nome} ({codigo_moeda_upper}/BRL) ---")
            print(f"Valor Atual (Compra): R$ {valor_atual:.4f}")
            print(f"Máximo do Dia: R$ {maximo:.4f}")
            print(f"Mínimo do Dia: R$ {minimo:.4f}")
            print(f"Última Atualização: {data_hora_formatada}")
        else:
            print(f"Não foi possível obter a cotação para {codigo_moeda_upper}-BRL. Verifique o código da moeda.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a AwesomeAPI: {e}")
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar os dados recebidos da API: {e}. O formato pode ter mudado ou a moeda é inválida.")

if __name__ == "__main__":
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ")
    if moeda:
        consultar_cotacao(moeda)
    else:
        print("Nenhum código de moeda fornecido.")