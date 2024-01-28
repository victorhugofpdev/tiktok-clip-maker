from pytube import YouTube
import os

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

    return f"{caminho_destino}/{nome_arquivo}.mp4"

path = script_download()