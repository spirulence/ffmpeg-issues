import ffmpeg


input_still = ffmpeg.input("../resources/still.jpg")
input_audio = ffmpeg.input("../resources/dance_beat.ogg")

(
    ffmpeg
    .concat(input_still, input_audio, v=1, a=1)
    .output("output.mp4")
    .run(overwrite_output=True)
)

