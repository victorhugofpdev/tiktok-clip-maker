from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip
import math

def download():

    # Insira o link do vídeo que você deseja baixar
    #link = input("Insira o link do vídeo: ")
    link = "https://youtu.be/uGTCi-e7RSA?si=aSu6xXSmwtaE6-Bo"

    # Criando um objeto YouTube com o link
    yt = YouTube(link)

    # Acessando a stream de maior resolução disponível
    ys = yt.streams.get_highest_resolution()

    # Solicitando ao usuário para inserir o nome do arquivo
    #nome_arquivo = input("Insira o nome do arquivo sem a extensão: ")
    nome_arquivo = "corte_dia_28"

    # Especificando o caminho de destino
    caminho_destino = "C:\\Users\\VH-vscode\\Desktop\\video_cortes"

    # Verificando se o diretório existe, se não, cria o diretório
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    # Iniciando o download com o nome e caminho do arquivo especificados
    print("Baixando...")
    ys.download(output_path=caminho_destino, filename=f"{nome_arquivo}.mp4")
    print("Download concluído!")


    return f"{caminho_destino}\\{nome_arquivo}.mp4"


def cortar_video(path, path_sat):
    # Extrai o nome base do vídeo sem a extensão
    nome_base = os.path.splitext(os.path.basename(path))[0]
    nome_base_sat = os.path.splitext(os.path.basename(path_sat))[0]
    # Define o diretório de saída para os clipes
    diretorio_saida = "C:\\Users\\VH-vscode\\Desktop\\clips"
    diretorio_saida_sat = "C:\\Users\\VH-vscode\\Desktop\\clips_sat"
    # Cria o diretório se ele não existir
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    if not os.path.exists(diretorio_saida_sat):
        os.makedirs(diretorio_saida_sat)

    
    # Carrega o vídeo
    clip = VideoFileClip(path)
    clip_2 = VideoFileClip(path_sat)
    duracao_total = clip.duration
    
    # Define a duração de cada segmento
    duracao_segmento_min = 60  # 1 minuto em segundos
    duracao_segmento_max = 130  # 2 minutos em segundos
    
    # Sobreposição de 20 segundos do segmento anterior
    sobreposicao = 10
    

    segmentos = []
    inicio = 0
    i = 0
    while inicio < duracao_total:
        # Define o fim do segmento, garantindo que não ultrapasse a duração total do vídeo
        fim = min(inicio + duracao_segmento_max, duracao_total)
        # Corta o segmento do vídeo
        segmento = clip.subclip(inicio, fim)
        segmento_sat = clip_2.subclip(inicio+20, fim+20)
        # Define o nome do arquivo de saída
        nome_do_arquivo = os.path.join(diretorio_saida, f"{nome_base}_parte_{i+1}.mp4")
        nome_do_arquivo_sat = os.path.join(diretorio_saida_sat, f"{nome_base_sat}_parte_{i+1}.mp4")
        # Salva o segmento
        segmento.write_videofile(nome_do_arquivo, codec="libx264")
        segmento_sat.write_videofile(nome_do_arquivo_sat, codec="libx264")
        
        segmentos.append(nome_do_arquivo)
        # Atualiza o início do próximo segmento, reduzindo-o pelos 20 segundos de sobreposição
        # exceto se for o fim do vídeo
        inicio = fim - (sobreposicao if fim < duracao_total else 0)
        i += 1
    
    return segmentos

def juntar_videos(path, path_sat, duration):
    # Carregar os vídeos
    video1 = VideoFileClip(path)
    video2 = VideoFileClip(path_sat).without_audio()

    # Verificar e ajustar a duração dos vídeos
    video2 = video2.subclip(0, duration)

    # Juntar os vídeos horizontalmente
    final_video =  CompositeVideoClip([video2, video1])


    path_final = "C:\\Users\\VH-vscode\\Desktop\\video_cortes"

    # Salvar o vídeo resultante
    final_video.write_videofile(path, codec="libx264", audio_codec="aac")

def download_sat():
    # Insira o link do vídeo que você deseja baixar
        
        #link = input("Insira o link do vídeo: ")
        link = 'https://youtu.be/vVJuMq1CMNo?si=EwggmsW0MWIVv9qR'

        # Criando um objeto YouTube com o link
        yt = YouTube(link)

        # Acessando a stream de maior resolução disponível
        ys = yt.streams.get_highest_resolution()

        # Solicitando ao usuário para inserir o nome do arquivo
        #nome_arquivo = input("Insira o nome do arquivo sem a extensão: ")
        nome_arquivo = 'clip_sat_1'

        # Especificando o caminho de destino
        caminho_destino = "C:\\Users\\VH-vscode\\Desktop\\video_sat"

        # Verificando se o diretório existe, se não, cria o diretório
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

        # Iniciando o download com o nome e caminho do arquivo especificados
        print("Baixando...")
        ys.download(output_path=caminho_destino, filename=f"{nome_arquivo}.mp4")
        print("Download concluído!")

        return f"{caminho_destino}\\{nome_arquivo}.mp4"



##  _____main______  ##


path = download()

path_sat = download_sat()

#clip = VideoFileClip(path)
#duration = clip.duration
#juntar_videos(path, path_sat, duration)

segmentos = cortar_video(path, path_sat)
print("Vídeos segmentados salvos em:", segmentos)
    





