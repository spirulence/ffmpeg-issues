import ffmpeg

(
    ffmpeg
    .input("../resources/video_with_audio.mp4")
    .output("more-metadata.mp4", metadata="title=METADATA MAN")
    .run(overwrite_output=True)
)

(
    ffmpeg
    .input("more-metadata.mp4")
    .output("less-metadata.mp4", map_metadata=-1)
    .run(overwrite_output=True)
)
