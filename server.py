from flask import Flask, request, send_file
from flask_cors import CORS  # ✅ enables cross-origin access
from gtts import gTTS
import io

app = Flask(__name__)
CORS(app, resources={r"/generate_voice": {"origins": "*"}})  # ✅ critical for CORS!

@app.route('/generate_voice', methods=['POST'])
def generate_voice():
    data = request.json
    text = data.get('text', '')

    # Convert to speech
    tts = gTTS(text, lang='en')
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    return send_file(audio_stream, mimetype='audio/mpeg')  # ✅ mp3 works too

if __name__ == '__main__':
    app.run()
