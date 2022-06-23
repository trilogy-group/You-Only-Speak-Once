import os
import sys
from moviepy.editor import VideoFileClip


def convert_video_to_audio_moviepy(video_file, output_ext="wav"):

    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


if __name__ == "__main__":
    vf = sys.argv[1]
    convert_video_to_audio_moviepy(vf)