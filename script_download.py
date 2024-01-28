from pytube import YouTube
import os
from moviepy.editor import VideoFileClip
import math

def script_download():

    # Insira o link do vídeo que você deseja baixar
    link = input("Insira o link do vídeo: ")

    # Criando um objeto YouTube com o link
    yt = YouTube(link)

    # Acessando a stream de maior resolução disponível
    ys = yt.streams.get_highest_resolution()

    # Solicitando ao usuário para inserir o nome do arquivo
    nome_arquivo = input("Insira o nome do arquivo sem a extensão: ")

    # Especificando o caminho de destino
    caminho_destino = "C:\\Users\\VH-vscode\\Documents\\video_cortes"

    # Verificando se o diretório existe, se não, cria o diretório
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    # Iniciando o download com o nome e caminho do arquivo especificados
    print("Baixando...")
    ys.download(output_path=caminho_destino, filename=f"{nome_arquivo}.mp4")
    print("Download concluído!")

    return f"{caminho_destino}\\{nome_arquivo}.mp4"



def cortar_video(path):
    # Extrai o nome base do vídeo sem a extensão
    nome_base = os.path.splitext(os.path.basename(path))[0]
    # Define o diretório de saída para os clipes
    diretorio_saida = "clips"
    
    # Cria o diretório se ele não existir
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    
    # Carrega o vídeo
    clip = VideoFileClip(path)
    duracao_total = clip.duration
    
    # Define a duração de cada segmento
    duracao_segmento_min = 60  # 1 minuto em segundos
    duracao_segmento_max = 120  # 2 minutos em segundos
    
    # Calcula o número de segmentos baseado na duração máxima
    numero_de_segmentos = math.ceil(duracao_total / duracao_segmento_max)
    
    segmentos = []
    for i in range(numero_de_segmentos):
        inicio = i * duracao_segmento_max
        fim = inicio + duracao_segmento_max
        if fim > duracao_total:
            fim = duracao_total
        
        # Garante que cada segmento tenha pelo menos a duração mínima, ajustando se necessário
        if fim - inicio < duracao_segmento_min:
            inicio = fim - duracao_segmento_min
        
        # Corta o segmento do vídeo
        segmento = clip.subclip(inicio, fim)
        
        # Define o nome do arquivo de saída
        nome_do_arquivo = os.path.join(diretorio_saida, f"{nome_base}_parte_{i+1}.mp4")
        
        # Salva o segmento
        segmento.write_videofile(nome_do_arquivo, codec="libx264")
        
        segmentos.append(nome_do_arquivo)
    
    return segmentos

# Exemplo de uso
path = script_download()


segmentos = cortar_video(path)
print("Vídeos segmentados salvos em:", segmentos)
    





