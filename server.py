from flask import Flask, request, send_file
from flask_cors import CORS
from gtts import gTTS
import io

app = Flask(__name__)

# ✅ Allow all origins (important for GitHub Pages)
CORS(app, resources={r"/generate_voice": {"origins": "*"}})

@app.route('/generate_voice', methods=['POST'])
def generate_voice():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return {"error": "No text provided"}, 400

    tts = gTTS(text, lang='en')
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    # ✅ Return MP3 audio stream
    return send_file(audio_stream, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run()
