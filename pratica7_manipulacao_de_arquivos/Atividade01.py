import pandas as pd
import os

def analisar_tempos_execucao(nome_arquivo='dados.csv', coluna_tempo='tempo_execucao'):
     
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
        print("Por favor, certifique-se de que o arquivo esteja no mesmo diretório do script")
        print("ou forneça o caminho completo para o arquivo.")
        return None, None

    try:
        # Lê o arquivo CSV para um DataFrame pandas
        df = pd.read_csv(nome_arquivo)

        # Verifica se a coluna de tempo de execução existe no DataFrame
        if coluna_tempo not in df.columns:
            print(f"Erro: A coluna '{coluna_tempo}' não foi encontrada no arquivo '{nome_arquivo}'.")
            print(f"Colunas disponíveis: {df.columns.tolist()}")
            print("Por favor, verifique o nome da coluna no seu arquivo CSV.")
            return None, None

        # Converte a coluna para tipo numérico (se já não for) e lida com valores não numéricos
        tempos_execucao = pd.to_numeric(df[coluna_tempo], errors='coerce').dropna()

        if tempos_execucao.empty:
            print(f"Atenção: A coluna '{coluna_tempo}' não contém dados numéricos válidos para cálculo.")
            return None, None

        # Calcula a média
        media = tempos_execucao.mean()

        # Calcula o desvio padrão
        desvio_padrao = tempos_execucao.std()

        return media, desvio_padrao

    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{nome_arquivo}' está vazio ou não contém dados.")
        return None, None
    except pd.errors.ParserError:
        print(f"Erro: Não foi possível analisar o arquivo '{nome_arquivo}'. Verifique o formato CSV.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")
        return None, None

# --- Parte principal do programa ---
if __name__ == "__main__":
    nome_do_arquivo_csv = 'dados.csv'
    nome_da_coluna_tempo = 'tempo_execucao'

    print(f"Analisando o arquivo: '{nome_do_arquivo_csv}'")
    print(f"Buscando a coluna de tempo de execução: '{nome_da_coluna_tempo}'")

    media_tempo, desvio_padrao_tempo = analisar_tempos_execucao(nome_do_arquivo_csv, nome_da_coluna_tempo)

    if media_tempo is not None and desvio_padrao_tempo is not None:
        print("\n--- Resultados ---")
        print(f"Média do tempo de execução: {media_tempo:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f}")
    else:
        print("\nNão foi possível calcular a média e o desvio padrão. Verifique as mensagens de erro acima.")