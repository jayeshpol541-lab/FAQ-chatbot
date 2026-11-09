import json, os
from flask import Flask, jsonify, render_template, request
from faq_engine import FAQEngine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "data", "faqs.json"), encoding="utf-8") as f:
    FAQS = json.load(f)

app = Flask(__name__)
engine = FAQEngine(FAQS)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Please type a question first."}), 400
    if len(message) > 500:
        return jsonify({"error": "Please keep your question under 500 characters."}), 400
    return jsonify(engine.get_answer(message))

@app.route("/api/faqs")
def faqs():
    return jsonify([{"question": x["question"], "category": x["category"]} for x in FAQS])

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "FAQ Chatbot"})

if __name__ == "__main__":
    app.run(debug=True)
