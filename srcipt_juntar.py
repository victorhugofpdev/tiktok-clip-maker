from moviepy.editor import VideoFileClip, clips_array
import os

def juntar_videos(path, path_sat, duration):
    # Carregar os vídeos
    video1 = VideoFileClip(path)
    video2 = VideoFileClip(path_sat)

    # Verificar e ajustar a duração dos vídeos
    video2 = video2.subclip(0, duration)

    # Juntar os vídeos horizontalmente
    final_video = clips_array([[video1, video2]])

    path_final = "C:\\Users\\VH-vscode\\Desktop\\video_cortes"

    # Salvar o vídeo resultante
    final_video.write_videofile(path_final, codec="libx264", audio_codec="aac")



juntar_videos(path, path_sat)
