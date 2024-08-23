import os
import sys
import time
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
import cv2
from video_processing import resize_video, get_video_duration, resize_video_with_cuda

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

app = Flask(__name__, template_folder='../templates')

UPLOAD_FOLDER = os.path.join(parent_dir, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key'  # Required to use flash messages

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        return f'File {filename} uploaded successfully'
    return redirect(request.url)

@app.route('/resize', methods=['POST'])
def resize_video_route():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)

        # Get resize parameters from the form
        width = request.form.get('width')
        height = request.form.get('height')
        interpolation = request.form.get('interpolation')
        codec = request.form.get('codec')
        use_gpu = 'use_gpu' in request.form

        # Validate width and height
        if width:
            width = int(width)
        if height:
            height = int(height)

        if not width and not height:
            flash('Either width or height must be provided')
            return redirect(request.url)

        interpolation = int(interpolation)

        # Generate improved output filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f'{filename.rsplit(".", 1)[0]}_{width}x{height}_{codec}_{timestamp}.mp4'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        # Estimate processing time
        duration = get_video_duration(input_path)
        estimated_time = duration * 0.5  # Example: 0.5 seconds per second of video
        flash(f'Estimated processing time: {int(estimated_time)} seconds')

        try:
            # Resize video with or without GPU
            if use_gpu and cv2.cuda.getCudaEnabledDeviceCount() > 0:
                resize_video_with_cuda(input_path, output_path, width=width, height=height, interpolation=interpolation, codec=codec)
            else:
                resize_video(input_path, output_path, width=width, height=height, interpolation=interpolation, codec=codec)
            
            flash(f'Video resized and saved as {output_filename}')
        except Exception as e:
            flash(f'Error occurred while resizing video: {str(e)}')
            return redirect(request.url)

        return redirect(url_for('home'))
    else:
        flash('Invalid file type')
        return redirect(request.url)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
