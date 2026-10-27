import json
import os

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

ENDPOINT = os.getenv('AZURE_CONTENT_UNDERSTANDING_ENDPOINT', '').strip()
KEY = os.getenv('AZURE_CONTENT_UNDERSTANDING_KEY', '').strip()
API_VERSION = os.getenv('AZURE_CONTENT_UNDERSTANDING_API_VERSION', '2025-11-01')
ANALYZERS = {'read': 'prebuilt-read', 'layout': 'prebuilt-layout', 'receipt': 'prebuilt-receipt'}
ALLOWED_TYPES = {'image/jpeg', 'image/png', 'image/webp', 'image/bmp', 'application/pdf'}


def analyze_bytes(data: bytes, content_type: str, analyzer_id: str) -> dict:
    if not ENDPOINT:
        raise ValueError('Configura AZURE_CONTENT_UNDERSTANDING_ENDPOINT en .env.')
    if KEY:
        credential = AzureKeyCredential(KEY)
    else:
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
    client = ContentUnderstandingClient(endpoint=ENDPOINT, credential=credential, api_version=API_VERSION)
    try:
        poller = client.begin_analyze_binary(
            analyzer_id=analyzer_id,
            binary_input=data,
            content_type=content_type,
        )
        result: AnalysisResult = poller.result()
        return result.as_dict()
    finally:
        client.close()


@app.get('/')
def index():
    return render_template('index.html', configured=bool(ENDPOINT))


@app.post('/analyze')
def analyze():
    upload = request.files.get('file')
    mode = request.form.get('mode', 'receipt')
    if not upload or not upload.filename:
        return jsonify(error='Selecciona una imagen o documento.'), 400
    if mode not in ANALYZERS:
        return jsonify(error='Selecciona un analizador válido.'), 400
    if upload.mimetype not in ALLOWED_TYPES:
        return jsonify(error='Formato no compatible. Usa JPG, PNG, WEBP, BMP o PDF.'), 400
    try:
        raw = upload.read()
        result = analyze_bytes(raw, upload.mimetype, ANALYZERS[mode])
        return jsonify(result=result, analyzer=ANALYZERS[mode], filename=upload.filename)
    except (AzureError, ValueError, OSError) as exc:
        return jsonify(error=str(exc)), 400
    except Exception as exc:
        return jsonify(error=f'No se pudo completar el análisis: {exc}'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.getenv('PORT', '5000')), debug=False)
