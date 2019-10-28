import ffmpeg

(
    ffmpeg
    .input("../resources/still.jpg")
    .filter("scale", "640", "-1")
    .output("output.jpg")
    .run(overwrite_output=True)
)
