from flask import Flask, redirect, url_for, request
from google_trans_new import google_translator
app = Flask(__name__)


@app.route("/", methods=["POST"])
def translate_text():
    json_data = request.json
    text = json_data['word']
    dest = json_data['dest']

    translator = google_translator()
    result = translator.translate("hello", lang_src="en", lang_tgt="es")

    return result
