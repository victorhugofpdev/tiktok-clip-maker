from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, CompositeVideoClip, AudioFileClip
import math
import cv2
import numpy as np

def download():
#'https://www.youtube.com/watch?v=FSIf6ZAFWyg','https://www.youtube.com/watch?v=6vgZm00MBUw'
    # Insira o link do vídeo que você deseja baixar
    #link = input("Insira o link do vídeo: ")
    lista_link = []
    lista_caminhos = []
    for link in lista_link:
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
        lista_caminhos.append(f"{caminho_destino}\\{nome_arquivo}.mp4")


    return lista_caminhos

def download_sat():
    # Insira o link do vídeo que você deseja baixar
        
        #link = input("Insira o link do vídeo: ")
    lista_link = ['https://www.youtube.com/watch?v=ebnQsTk9s-s']
    lista_caminhos = []
    for link in lista_link:
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
            lista_caminhos.append(f"{caminho_destino}\\{nome_arquivo}.mp4")

    return lista_caminhos

def cortar_video(path, path_sat):
    adicional_de_duracao = 0
    # Extrai o nome base do vídeo sem a extensão
    nome_base = os.path.splitext(os.path.basename(path))[0]
    nome_base_sat = os.path.splitext(os.path.basename(path_sat))[0]
    # Define o diretório de saída para os clipes
    diretorio_saida = "C:\\Users\\VH-vscode\\Desktop\\clips"
    diretorio_saida_sat = "C:\\Users\\VH-vscode\\Desktop\\clips_sat"
    diretorio_saida_audio = "C:\\Users\\VH-vscode\\Desktop\\clips_audio"
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
    duracao_segmento_max = 130  # 2 minutos e 10 segundos em segundos

    # Sobreposição de 10 segundos do segmento anterior
    sobreposicao = 10

    inicio = 0
    i = 0
    lista_clips = []
    lista_clips_sat = []
    lista_audio_clips = []

    while inicio < duracao_total:
        # Define o fim do segmento, garantindo que não ultrapasse a duração total do vídeo
        fim = min(inicio + duracao_segmento_max, duracao_total)
        # Corta o segmento do vídeo
        segmento = clip.subclip(inicio , fim )
        segmento_sat = clip_2.subclip(inicio+20, fim+20).without_audio()  # Removido o +20 para alinhamento correto

        # Define o nome do arquivo de saída
        nome_do_arquivo = os.path.join(diretorio_saida, f"{nome_base}_parte_{i+1}.mp4")
        nome_do_arquivo_sat = os.path.join(diretorio_saida_sat, f"{nome_base_sat}_parte_{i+1}.mp4")
        nome_do_arquivo_audio = os.path.join(diretorio_saida_audio, f"{nome_base}_audio_parte_{i+1}.mp3")

        lista_clips.append(nome_do_arquivo)
        lista_clips_sat.append(nome_do_arquivo_sat)
        lista_audio_clips.append(nome_do_arquivo_audio)
        # Salva o segmento
        segmento.write_videofile(nome_do_arquivo, codec="libx264")
        segmento_sat.write_videofile(nome_do_arquivo_sat, codec="libx264")
        segmento.audio.write_audiofile(nome_do_arquivo_audio)  # Correção aqui, sem especificar codec para áudio

        # Atualiza o início do próximo segmento, reduzindo-o pelos segundos de sobreposição
        inicio = fim - (sobreposicao if fim < duracao_total else 0)
        i += 1
        '''if segmento.duration > duracao_segmento_min:
            i += 1
            continue
        else:
            adicional_de_duracao = segmento.duration/i
            fim = fim + adicional_de_duracao '''  
    return lista_clips, lista_clips_sat, lista_audio_clips

def juntar_video(path_, path_sat_, clips_audio_path_):
    i = 0
    for path, path_sat, clips_audio_path in zip(path_, path_sat_, clips_audio_path_):
        # Abrir os vídeos
        cap1 = cv2.VideoCapture(path)
        cap2 = cv2.VideoCapture(path_sat)

        # Propriedades do vídeo de saída
        frame_width = int(cap1.get(3))
        frame_height = int(cap1.get(4))

        # Ajustar a altura para a metade, pois cada vídeo ocupará metade da tela
        frame_height_adjusted = frame_height // 2

        out = cv2.VideoWriter(f'C:\\Users\\VH-vscode\\Desktop\\clips\\video_resultado_{i+1}.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30, (frame_width, frame_height))

        while cap1.isOpened() and cap2.isOpened():
            ret1, frame1 = cap1.read()
            ret2, frame2 = cap2.read()
            
            if ret1 and ret2:
                # Redimensionar os frames para caberem na metade superior e inferior da tela
                frame1_resized = cv2.resize(frame1, (frame_width, frame_height_adjusted))
                frame2_resized = cv2.resize(frame2, (frame_width, frame_height_adjusted))
                
                # Combinar os frames verticalmente
                combined_frame = np.vstack((frame1_resized, frame2_resized))
                
                # Escrever o frame combinado no vídeo de saída
                out.write(combined_frame)
            else:
                break
        # Liberar os recursos
        cap1.release()
        cap2.release()
        out.release()
        audio_video(clips_audio_path, i)
        i += 1

def audio_video(clips_audio_path, i):

    # Caminho para o arquivo de vídeo original
    caminho_video = f'C:\\Users\\VH-vscode\\Desktop\\clips\\video_resultado_{i+1}.mp4'
    # Caminho para o arquivo de áudio que você deseja adicionar ao vídeo
    caminho_audio = clips_audio_path

    # Carrega o vídeo
    video_clip = VideoFileClip(caminho_video)
    # Carrega o áudio
    audio_clip = AudioFileClip(caminho_audio)

    # Define a duração do áudio igual à duração do vídeo
    audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Define o áudio do vídeo para ser o áudio carregado
    video_clip = video_clip.set_audio(audio_clip)

    # Especifica o nome do arquivo de saída para o vídeo com o novo áudio
    nome_arquivo_saida = f'C:\\Users\\VH-vscode\\Desktop\\clips\\video_{i+1}.mp4'

    # Escreve o arquivo de vídeo com o novo áudio
    video_clip.write_videofile(nome_arquivo_saida, codec="libx264", audio_codec="aac")

##  _____main______  ##
lista_path = download()
lista_path_sat = download_sat()

for path, path_sat in zip(lista_path, lista_path_sat):
    segmentos, segmentos_sat, clips_audio_path = cortar_video(path, path_sat)
    #juntar_video(segmentos, segmentos_sat, clips_audio_path)





    





