from flask import Flask, request, send_file
from flask_cors import CORS   # ✅ Add this
from gtts import gTTS
import io

app = Flask(__name__)
CORS(app)   # ✅ Add this

@app.route('/generate_voice', methods=['POST'])
def generate_voice():
    data = request.json
    text = data.get('text', '')

    # Convert text to speech
    tts = gTTS(text, lang='en')
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    # Return as mp3 stream
    return send_file(audio_stream, mimetype='audio/mp3')

if __name__ == '__main__':
    app.run()
