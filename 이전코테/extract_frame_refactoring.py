import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=30):
    """
    Extract frames from a video file at a specified frame rate.

    :param video_path: Path to the video file
    :param output_folder: Folder to save the extracted frames
    :param frame_rate: Number of frames per second to extract
    """
    # Get the base name of the video file without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_folder = os.path.join(output_folder, video_name)
    os.makedirs(video_output_folder, exist_ok=True)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get the video frame rate
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps == 0:
        print("Error: Unable to fetch video frame rate.")
        cap.release()
        return

    # Calculate the frame interval to match the desired frame rate
    frame_interval = int(video_fps / frame_rate)

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame if it matches the interval
        if frame_count % frame_interval == 0:
            output_file = os.path.join(video_output_folder, f"{video_name}_{saved_count:06d}.jpg")
            cv2.imwrite(output_file, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames from {video_path} to {video_output_folder}")

def process_directory(input_directory, output_directory, frame_rate=30):
    """
    Process all .mp4 and .mov files in a directory (and subdirectories),
    extracting frames at a specified frame rate.

    :param input_directory: Path to the input directory containing videos
    :param output_directory: Path to the output directory for extracted frames
    :param frame_rate: Number of frames per second to extract
    """
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith(('.mp4', '.mov')):
                video_path = os.path.join(root, file)
                print(f"Processing {video_path}...")
                extract_frames(video_path, output_directory, frame_rate)

# Example usage
input_dir = "videos"  # Replace with your input directory
output_dir = "frames_output"  # Replace with your desired output directory
process_directory(input_dir, output_dir, 30)
