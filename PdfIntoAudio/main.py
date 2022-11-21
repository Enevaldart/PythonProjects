from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from script import convert
import pyttsx3


app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            save_location = os.path.join('uploads', filename)
            save_location = save_location.replace(' ', '_')
            save_location = save_location.replace('\\', '/')
            file.save(save_location)

            output_file = convert(save_location)
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#running the speech engine on testing
@app.route('/send_data', methods=['POST'])
def test_speech():
  try:
    if request.method == 'POST':
        test_text = request.form['test_text']
        voice_choice = request.form['voice_choice']
        if voice_choice == 'female':
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)
        speech_rate = request.form['speech_rate']
        engine.setProperty('rate', speech_rate)
        engine.say(test_text)
        engine.runAndWait()
  except:
    return 'something went wrong'

#saving input speech from the testing input box
@app.route('/save_speech/', methods=['GET', 'POST'])
def save_speech():
    if request.method == 'POST':
        test_text = request.form['test_text']
        speech_rate = request.form['speech_rate']
        engine.setProperty('rate', speech_rate)
        voice_choice = request.form['voice_choice']
        if voice_choice == 'female':
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[0].id)
        engine.save_to_file(test_text, 'test1.mp3')
        engine.runAndWait()
        engine.say(test_text)
    return'saving ..'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
