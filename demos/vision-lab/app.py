import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv(override=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB

endpoint = os.getenv("VISION_ENDPOINT")
key = os.getenv("VISION_KEY")

client = None
if endpoint and key:
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )


@app.get("/")
def index():
    return render_template("index.html", configured=client is not None)


@app.post("/analyze")
def analyze():
    if client is None:
        return jsonify({
            "error": "Falta configurar VISION_ENDPOINT o VISION_KEY en el archivo .env."
        }), 500

    if "image" not in request.files:
        return jsonify({"error": "Selecciona una imagen para analizar."}), 400

    image = request.files["image"]
    if not image.filename:
        return jsonify({"error": "Selecciona una imagen para analizar."}), 400

    try:
        result = client.analyze(
            image_data=image.read(),
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
            ],
            gender_neutral_caption=True,
        )

        caption = None
        confidence = None
        if result.caption:
            caption = result.caption.text
            confidence = round(result.caption.confidence * 100)

        tags = []
        if result.tags:
            tags = [
                {
                    "name": tag.name,
                    "confidence": round(tag.confidence * 100),
                }
                for tag in result.tags.list[:8]
            ]

        objects = []
        if result.objects:
            for detected in result.objects.list[:8]:
                if detected.tags:
                    objects.append(detected.tags[0].name)

        return jsonify({
            "caption": caption,
            "confidence": confidence,
            "tags": tags,
            "objects": objects,
        })

    except Exception as error:
        app.logger.exception("Error al analizar la imagen")
        return jsonify({
            "error": f"Azure AI Vision no pudo analizar la imagen: {error}"
        }), 502


@app.errorhandler(413)
def too_large(_error):
    return jsonify({"error": "La imagen supera el límite de 20 MB."}), 413


if __name__ == "__main__":
    app.run(debug=True)