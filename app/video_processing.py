import cv2
import numpy as np

def resize_video(input_path, output_path, width=None, height=None, interpolation=cv2.INTER_LINEAR, codec='mp4v'):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError("Could not open the video file.")

    fourcc = cv2.VideoWriter_fourcc(*codec)
    
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if width and not height:
        height = int(width * original_height / original_width)
    elif height and not width:
        width = int(height * original_width / original_height)
    elif not width and not height:
        width, height = original_width, original_height

    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (width, height), interpolation=interpolation)
        out.write(resized_frame)

    cap.release()
    out.release()

def get_video_duration(input_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError("Could not open the video file.")
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    cap.release()
    return duration

def resize_video_with_cuda(input_path, output_path, width=None, height=None, interpolation=cv2.INTER_LINEAR, codec='mp4v'):
    if not cv2.cuda.getCudaEnabledDeviceCount():
        raise RuntimeError("CUDA is not available. Cannot use GPU acceleration.")

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError("Could not open the video file.")

    fourcc = cv2.VideoWriter_fourcc(*codec)
    
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if width and not height:
        height = int(width * original_height / original_width)
    elif height and not width:
        width = int(height * original_width / original_height)
    elif not width and not height:
        width, height = original_width, original_height

    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

    gpu_stream = cv2.cuda_Stream()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gpu_frame = cv2.cuda_GpuMat(frame)
        resized_gpu_frame = cv2.cuda.resize(gpu_frame, (width, height), interpolation=interpolation, stream=gpu_stream)
        resized_frame = resized_gpu_frame.download()
        out.write(resized_frame)

    cap.release()
    out.release()