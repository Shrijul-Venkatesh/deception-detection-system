import os
from moviepy.editor import VideoFileClip

# Define the input and output directories
input_dir = "video_set"
output_dir = "audio_set"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the video file extensions to look for
video_extensions = [
    ".wmv",
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
]

# Get a list of all video files in the input directory
video_files = [
    f
    for f in os.listdir(input_dir)
    if os.path.splitext(f)[1].lower() in video_extensions
]

for video_file in video_files:
    input_path = os.path.join(input_dir, video_file)

    video = VideoFileClip(input_path)

    audio = video.audio

    base_name = os.path.splitext(video_file)[0]
    audio_output_path = os.path.join(output_dir, f"{base_name}_audio.mp3")

    audio.write_audiofile(audio_output_path)

print("Processing completed.")
