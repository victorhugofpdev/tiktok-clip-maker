from pytube import YouTube

# Insira o link do vídeo que você deseja baixar
link = input("Insira o link do vídeo: ")

# Criando um objeto YouTube com o link
yt = YouTube(link)

# Acessando a stream de maior resolução disponível
ys = yt.streams.get_highest_resolution()

# Solicitando ao usuário para inserir o nome do arquivo
nome_arquivo = input("Insira o nome do arquivo sem a extensão: ")

# Iniciando o download com o nome do arquivo especificado
print("Baixando...")
ys.download(filename=f"{nome_arquivo}.mp4")
print("Download concluído!")
