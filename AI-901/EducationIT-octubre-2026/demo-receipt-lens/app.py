import base64
import json
import os
import re
from datetime import datetime

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

VISION_ENDPOINT = os.getenv("VISION_ENDPOINT", "").rstrip("/")
VISION_KEY = os.getenv("VISION_KEY", "")
VISION_API_VERSION = os.getenv("VISION_API_VERSION", "2024-02-01")


def read_image(image_bytes: bytes) -> str:
    if not VISION_ENDPOINT or not VISION_KEY:
        raise ValueError("Configura VISION_ENDPOINT y VISION_KEY en el archivo .env.")

    url = f"{VISION_ENDPOINT}/computervision/imageanalysis:analyze"
    response = requests.post(
        url,
        params={"api-version": VISION_API_VERSION, "features": "read"},
        headers={"Ocp-Apim-Subscription-Key": VISION_KEY,
                 "Content-Type": "application/octet-stream"},
        data=image_bytes,
        timeout=60,
    )
    if not response.ok:
        raise RuntimeError(f"Azure Vision respondió {response.status_code}: {response.text[:500]}")

    data = response.json()
    lines = []
    for block in data.get("readResult", {}).get("blocks", []):
        for line in block.get("lines", []):
            lines.append(line.get("text", ""))
    return "\n".join(line for line in lines if line)


def extract_receipt_fields(text: str) -> dict:
    """Extracción didáctica basada en patrones; los resultados deben verificarse."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    joined = "\n".join(lines)

    def find(pattern, flags=re.IGNORECASE | re.MULTILINE):
        match = re.search(pattern, joined, flags)
        return match.group(1).strip() if match else "No identificado"

    date = find(r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2})\b")
    phone = find(r"(?:tel(?:éfono)?\s*[:.]?\s*)?(\+?\d[\d ()-]{7,}\d)")
    total = find(r"(?:total|amount\s+due|grand\s+total)\s*[:$ ]*([$€£]?\s?\d+[.,]\d{2})")
    tax = find(r"(?:tax|iva|impuesto)\s*[:$ ]*([$€£]?\s?\d+[.,]\d{2})")
    subtotal = find(r"(?:subtotal|sub-total)\s*[:$ ]*([$€£]?\s?\d+[.,]\d{2})")

    merchant = next((line for line in lines[:4] if not re.search(r"\d{5,}", line)), "No identificado")
    currency_match = re.search(r"([$€£])", joined)
    return {
        "comercio": merchant,
        "fecha": date,
        "telefono": phone,
        "subtotal": subtotal,
        "impuestos": tax,
        "total": total,
        "moneda_detectada": currency_match.group(1) if currency_match else "No identificada",
        "nota": "Extracción demostrativa por patrones sobre el texto OCR. Verifica los valores; para producción usa Document Intelligence o Content Understanding.",
    }


@app.get("/")
def index():
    return render_template("index.html", configured=bool(VISION_ENDPOINT and VISION_KEY))


@app.post("/analyze")
def analyze():
    image = request.files.get("image")
    mode = request.form.get("mode", "receipt")
    if not image or not image.filename:
        return jsonify(error="Selecciona una imagen para analizar."), 400
    if image.mimetype not in {"image/jpeg", "image/png", "image/webp", "image/bmp"}:
        return jsonify(error="Formato no compatible. Usa JPG, PNG, WEBP o BMP."), 400
    try:
        raw = image.read()
        text = read_image(raw)
        result = {"text": text or "No se detectó texto legible.", "fields": extract_receipt_fields(text) if mode == "receipt" else None}
        result["preview"] = f"data:{image.mimetype};base64,{base64.b64encode(raw).decode()}"
        return jsonify(result)
    except (ValueError, RuntimeError, requests.RequestException) as exc:
        return jsonify(error=str(exc)), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
