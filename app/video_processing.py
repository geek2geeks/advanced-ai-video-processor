import cv2

def resize_video(input_path, output_path, width=None, height=None, interpolation=cv2.INTER_LINEAR):
    """
    Resize a video while maintaining its aspect ratio.

    :param input_path: Path to the input video file.
    :param output_path: Path to save the resized video.
    :param width: Desired width of the resized video. If None, height will be used to calculate width.
    :param height: Desired height of the resized video. If None, width will be used to calculate height.
    :param interpolation: Interpolation method used for resizing.
    """
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' for .avi
    
    if not cap.isOpened():
        raise ValueError("Could not open the video file.")

    # Get original dimensions
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Calculate new dimensions
    if width and not height:
        aspect_ratio = original_height / original_width
        height = int(width * aspect_ratio)
    elif height and not width:
        aspect_ratio = original_width / original_height
        width = int(height * aspect_ratio)
    elif not width and not height:
        width, height = original_width, original_height

    # Set up the video writer
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (width, height), interpolation=interpolation)
        out.write(resized_frame)

    cap.release()
    out.release()
