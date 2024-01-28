from moviepy.editor import VideoFileClip, clips_array

def juntar_videos(video1_path, video2_path, output_path):
    # Carregar os vídeos
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)

    # Verificar e ajustar a duração dos vídeos
    min_duration = min(video1.duration, video2.duration)
    video1 = video1.subclip(0, min_duration)
    video2 = video2.subclip(0, min_duration)

    # Juntar os vídeos horizontalmente
    final_video = clips_array([[video1, video2]])

    # Salvar o vídeo resultante
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    video1_path = "caminho/do/video1.mp4"
    video2_path = "caminho/do/video2.mp4"
    output_path = "caminho/do/video_final.mp4"

    juntar_videos(video1_path, video2_path, output_path)
