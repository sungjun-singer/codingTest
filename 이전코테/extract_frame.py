import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=30):
    """
    Extract frames from a video file at a specified frame rate.

    :param video_path: Path to the video file
    :param output_folder: Folder to save the extracted frames
    :param frame_rate: Number of frames per second to extract
    """
    # Check if the output folder exists, and create it if it doesn't
    os.makedirs(output_folder, exist_ok=True)

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
            output_file = os.path.join(output_folder, f"frame_{saved_count:06d}.jpg")
            cv2.imwrite(output_file, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames from {video_path} to {output_folder}")

# Example usage
video_file = "videos/001_iPhone13_60.mov"  # Replace with your video file
output_directory = "frames_output"  # Replace with your desired output folder
extract_frames(video_file, output_directory, 60)
