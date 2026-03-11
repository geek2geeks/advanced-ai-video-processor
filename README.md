# Advanced AI Video Processor

**Status:** Production-Ready Service | **Domain:** Computer Vision, Video Enhancement

A comprehensive web application and backend service dedicated to high-quality video enhancement. By leveraging state-of-the-art Deep Learning models like RIFE (Real-Time Intermediate Flow Estimation) alongside robust OpenCV processing, this system enables users to seamlessly upscale the framerate (FPS) of videos and dynamically resize streams without compromising visual fidelity.

## 🎯 Technical Highlights
- **AI-Driven Frame Interpolation:** Integrated the PyTorch-based RIFE model to synthesize intermediate frames, effectively doubling or quadrupling video framerates to create ultra-smooth slow-motion or high-FPS outputs.
- **Robust Video Processing Pipeline:** Architected a pipeline combining OpenCV for frame manipulation (resizing, aspect-ratio preservation) and FFmpeg for highly efficient H.265 (HEVC) encoding, optimizing storage and playback quality.
- **Extensible Web Interface:** Built a Flask-based frontend with secure video upload mechanisms, allowing users to intuitively select target resolutions and framerates.
- **Scalable Architecture:** Designed the codebase modularly, separating routing (`app/main.py`), core processing logic, and model inference, making it trivial to drop in new AI models (e.g., Super-Resolution or Video Stabilization).

## 🏗 Architecture & Flow
1. **Upload & Validation:** Videos (MP4, AVI, MOV) are securely uploaded via the web interface and staged in temporary storage.
2. **Preprocessing:** OpenCV evaluates the input stream, extracting frame dimensions, original FPS, and codec information. If resizing is requested, frames are processed while strictly maintaining the aspect ratio.
3. **AI Inference Pipeline:**
   - The stream is batched and fed into the RIFE optical flow model.
   - The model estimates intermediate motion vectors and synthesizes new, realistic frames between the original frames.
4. **Encoding:** The enhanced frame sequence is passed to FFmpeg and encoded using H.265 to significantly compress the enhanced video size without noticeable quality degradation.

## 💻 Tech Stack
- **Core AI:** PyTorch, RIFE (Optical Flow Frame Interpolation)
- **Computer Vision:** OpenCV, FFmpeg
- **Backend/API:** Python 3.9+, Flask
- **Testing:** Pytest

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- FFmpeg (Installed and available in the system PATH)
- Virtual Environment tool

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/geek2geeks/advanced-ai-video-processor.git
   cd advanced-ai-video-processor
   ```
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the Flask application:
   ```bash
   export FLASK_APP=app.main  # On Windows: set FLASK_APP=app.main
   flask run
   ```
2. Navigate to `http://127.0.0.1:5000/` in your browser.

## 🧪 Testing
The project includes automated unit tests for video processing features to ensure stability before deployment.
```bash
pytest tests/
```

## 📈 Future Enhancements
- **Asynchronous Task Queues:** Implement Celery and Redis to handle long-running video processing tasks in the background, freeing up the web server.
- **TensorRT Optimization:** Export the PyTorch RIFE model to TensorRT to maximize inference throughput on NVIDIA GPUs.
- **Super-Resolution Models:** Integrate models like Real-ESRGAN to provide upscaling (e.g., 1080p to 4K) alongside frame interpolation.