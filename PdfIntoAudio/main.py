import threading
import time
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from script import convert
from speech import text_to_speech
import pyttsx3
from flask_cors import cross_origin
from flask import send_file


app = Flask(__name__)

engine = pyttsx3.init()
ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
        return render_template('index.html')


@app.route("/convert_pdf", methods=['GET', 'POST'])
def convert_pdf():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_location = os.path.join('uploads', filename)
            save_location = save_location.replace(' ', '_')
            save_location = save_location.replace('\\', '/')
            file.save(save_location)

            convert(save_location)

            save_location = save_location.replace('pdf', 'mp3')
            save_location = save_location.replace('uploads', 'downloads')
            path = save_location
            return send_file(path, as_attachment=True)
    return 'It seems you entered non-pdf file'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
