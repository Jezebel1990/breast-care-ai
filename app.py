from flask import Flask, jsonify, render_template
from resultados import calcular_metricas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/resultados")
def api_resultados():
    metrics = calcular_metricas()
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(debug=True)

