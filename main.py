from moviepy.editor import VideoFileClip
import pytube
import os


def download_video(url):
    # Realiza o download do vídeo usando a biblioteca pytube
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download()

def convert_to_mp4(filename):
    # Converte o vídeo para o formato MP4 usando a biblioteca moviepy
    video = VideoFileClip(filename)
    video.write_videofile("output.mp4")

# URL do vídeo que deseja baixar
video_url = "hhttps://www.youtube.com/watch?v=6qSC6D9x62o"

# Baixa o vídeo
download_video(video_url)

# Nome do arquivo de vídeo baixado
filename = "Cariane.mp4"

# Converte o vídeo para o formato MP4
convert_to_mp4(filename)


video_path = '/Users/pedrohenriqueribeiro/Desktop/Video Cutter/videos'
output_directory = '/Users/pedrohenriqueribeiro/Desktop/Video Cutter/cortes'
def split_video(video_path, output_directory):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    min_duration = 60  # 1 minuto em segundos
    max_duration = 120  # 2 minutos em segundos
    start_time = 0
    end_time = min_duration

    video_number = 1

    while end_time <= duration:
        subclip = clip.subclip(start_time - 5, end_time)
        subclip.write_videofile(os.path.join(output_directory, f'video_{video_number}.mp4'))

        start_time = end_time - 5
        end_time += min_duration

        if end_time + min_duration > duration:
            end_time = duration

        video_number += 1

    clip.close()

os.path.join(output_directory, f'video_{video_number}.mp4')


