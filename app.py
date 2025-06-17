from flask import Flask, jsonify, render_template
from resultados import calcular_metricas
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/resultados")
def api_resultados():
    metrics = calcular_metricas()
    return jsonify(metrics)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
