import ffmpeg


input_video = ffmpeg.input("../resources/video_with_audio.mp4")
added_audio = ffmpeg.input("../resources/dance_beat.ogg").audio.filter('adelay', "1500|1500")

merged_audio = ffmpeg.filter([input_video.audio, added_audio], 'amix')

(
    ffmpeg
    .concat(input_video, merged_audio, v=1, a=1)
    .output("mix_delayed_audio.mp4")
    .run(overwrite_output=True)
)

