import os
from moviepy.editor import VideoFileClip

# Define the input and output directories
input_dir = "Videos"
output_dir = "Output"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all video files in the input directory
video_extensions = ['.wmv', '.mp4', '.avi', '.mov', '.mkv']  # Add more extensions as needed
video_files = [f for f in os.listdir(input_dir) if os.path.splitext(f)[1].lower() in video_extensions]

for video_file in video_files:
    input_path = os.path.join(input_dir, video_file)
    
    # Load the video file
    video = VideoFileClip(input_path)
    
    # Extract the audio
    audio = video.audio
    
    # Define the output paths
    base_name = os.path.splitext(video_file)[0]
    audio_output_path = os.path.join(output_dir, f"{base_name}_audio.mp3")
    video_output_path = os.path.join(output_dir, f"{base_name}_video.mp4")
    
    # Save the audio
    audio.write_audiofile(audio_output_path)
    
    # Save the video without audio
    video.without_audio().write_videofile(video_output_path)

print("Processing completed.")
