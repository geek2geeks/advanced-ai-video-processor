# Advanced AI Video Processor

## Overview
Advanced AI Video Processor is a web application built using Flask, OpenCV, and PyTorch. It provides users with the ability to upload videos, resize them, and perform advanced AI-based frame interpolation to increase FPS (frames per second). The application is designed to be extensible and can be used as a foundation for more complex video processing tasks.

## Key Features
- **Secure Video Upload**: Allows users to upload videos in common formats (MP4, AVI, MOV) securely.
- **Video Resizing**: Uses OpenCV to resize videos while maintaining aspect ratio.
- **AI-Based Frame Interpolation**: Implements AI models like RIFE (Real-Time Intermediate Flow Estimation) for smooth frame interpolation, increasing the FPS of a video.
- **H.265 Encoding**: Uses FFmpeg for efficient video encoding.

## Project Structure
```
advanced-ai-video-processor/
├── .gitignore              # Ignore files for Git
├── app/
│   └── main.py             # Main Flask application code
├── LICENSE                 # License file
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── static/
│   └── uploads/            # Directory to store uploaded files
└── templates/
    └── index.html          # HTML template for the upload page
```

## Folder and File Descriptions
- `app/main.py`: The core of the Flask application. It handles routing, video processing logic, and integrates the AI model.
- `static/uploads/`: Directory where uploaded videos are temporarily stored.
- `templates/index.html`: The HTML template that serves the video upload form.
- `requirements.txt`: Contains the list of Python dependencies required to run the project.

## Setup Instructions
### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment tool (e.g., venv, virtualenv, or conda)
- Git (for cloning the repository)
- FFmpeg (Ensure FFmpeg is installed and added to your system's PATH)

### Installation
1. Clone the Repository:
   ```bash
   git clone https://github.com/geek2geeks/advanced-ai-video-processor.git
   cd advanced-ai-video-processor
   ```
2. Set Up a Virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```
3. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install FFmpeg:
   - Download and install FFmpeg from [here](https://ffmpeg.org/download.html).
   - Ensure FFmpeg is added to your system's PATH.

## Running the Application
1. Set the Flask Application Environment Variable:
   ```bash
   set FLASK_APP=app.main  # For Windows
   export FLASK_APP=app.main  # For Unix/Mac
   ```
2. Run the Flask Application:
   ```bash
   flask run
   ```
3. Access the Application:
   - Open your browser and go to `http://127.0.0.1:5000/`.
   - You should see the upload page where you can select a video file to upload and process.

## Usage
### Uploading a Video
1. On the main page, use the "Choose File" button to select a video file from your local machine.
2. Click the "Upload" button to upload the video to the server.
3. The server will process the video based on the options provided (e.g., resizing or frame interpolation).

### Video Resizing
1. Once the video is uploaded, you can choose the desired resolution or aspect ratio for resizing.
2. The server processes the video using OpenCV, preserving the aspect ratio during resizing.

### AI Frame Interpolation
1. Specify the target FPS you want to achieve.
2. The server will use the pre-trained RIFE model to interpolate frames and increase the video FPS.

### Video Encoding
After processing, the video is encoded using H.265 (HEVC) for efficient storage and playback.

## Testing
### Running Unit Tests
Unit tests are included to verify the functionality of the video processing features.

Run the tests using pytest:
```bash
pytest tests/
```
Ensure all tests pass before deploying or sharing the application.

## Troubleshooting
### Common Issues
#### TemplateNotFound Error
- Ensure that the `templates/` directory is correctly located relative to the application.
- Verify that the environment variables and paths are correctly set.

#### FFmpeg Not Found
- Ensure FFmpeg is installed and added to your system's PATH.
- Restart your terminal or command prompt after installing FFmpeg.

### Logging
The application includes basic logging to help debug issues. Logs can be found in the terminal where the application is running.

## Contributing
### How to Contribute
1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/advanced-ai-video-processor.git
   ```
3. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and commit them with a descriptive message:
   ```bash
   git commit -m "Description of your changes"
   ```
5. Push your changes to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Create a Pull Request on the original repository and describe the changes you've made.

### Code of Conduct
Please adhere to the project's code of conduct in all interactions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework in Python.
- [OpenCV](https://opencv.org/): A library of programming functions mainly aimed at real-time computer vision.
- [PyTorch](https://pytorch.org/): An open-source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing.

## Future Work
- **User Authentication**: Implement user authentication and session management.
- **Video Persistence**: Add functionality to save processed videos between sessions.
- **Additional AI Models**: Integrate other AI models for video processing, such as super-resolution or video stabilization.