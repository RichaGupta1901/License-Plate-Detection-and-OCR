from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
from License_detect import detect_license_plate_ocr


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "No image uploaded!", 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(image_path)

    # Run detection
    output_path, plate_texts = detect_license_plate_ocr(image_path)

    return render_template("result.html", original=filename, output=os.path.basename(output_path), plates=plate_texts)

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
