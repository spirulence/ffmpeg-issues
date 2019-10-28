import ffmpeg

(
    ffmpeg
    .input('../resources/video_with_audio.mp4')
    .output('image-%06d.jpg')
    .run()
)