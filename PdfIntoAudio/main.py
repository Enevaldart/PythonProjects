import threading
import time
from flask import Flask, render_template,  request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os, shutil
from script import convert
from speech import text_to_speech
import pyttsx3
from flask_cors import cross_origin
from flask import send_file
from flask import after_this_request


app = Flask(__name__)

engine = pyttsx3.init()
ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
        return render_template('index.html')


@app.route('/Behind_the_making', methods=['GET', 'POST'])
def behind_the_making():
    return render_template('Profile.html')


@app.route('/Terms_of_service', methods=['GET', 'POST'])
def Terms_of_service():
    return render_template('terms.html')


@app.route("/convert_pdf", methods=['GET', 'POST'])
def convert_pdf():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestr = time.strftime("%Y%m%d_%H%M%S")

            save_location = os.path.join('uploads', filename)
            save_location = save_location.replace(' ', '_')
            save_location = save_location.replace('\\', '/')
            save_location = save_location.replace('.pdf', '_listenToPdf' + timestr + '.pdf')
            file.save(save_location)

            convert(save_location)

            save_location = save_location.replace('pdf', 'mp3')
            save_location = save_location.replace('uploads', 'downloads')
            file_path = save_location
            file_handle = open(file_path, 'r')
            file_handle.close()

            try:
                return send_file(file_path, as_attachment=True)
            finally:
                folder = 'downloads'
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('failed to delete %s. Reason: %s' % (file_path, e))
                print('Audio deleted!')
                folder2 = 'uploads'
                for filename in os.listdir(folder2):
                    file_path = os.path.join(folder2, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('failed to delete %s. Reason: %s' % (file_path, e))
                print('Pdf deleted!')


    return render_template('wrongfile.html')


if __name__ == "__main__":
    app.run()
