from flask import Flask, render_template, request, jsonify
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sallmon.frontend.models import db
#from models import db
from sallmon.frontend.routes.metrics import metrics_bp
from sallmon.frontend.routes.wallets import wallets_bp
import requests  # <-- Ensure this is imported
import subprocess

BASE_URL = "http://127.0.0.1:1337"  # Replace with your actual backend API URL

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DB_PATH = os.path.expanduser("~/.sallmon/wallet.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db.init_app(app)

# Register blueprints
app.register_blueprint(metrics_bp, url_prefix="/metrics")
app.register_blueprint(wallets_bp, url_prefix="/wallets")

@app.route("/")
def home():
    """Node Control Dashboard"""
    return render_template("node_dashboard.html")

SALLMON_SERVER_CMD = "sallmon-server"



from flask import Response
import subprocess
import threading

SALLMON_SERVER_CMD = "python3 -m sallmon.frontend.server"

@app.route("/start-node", methods=["POST"])
def start_node():
    """Start the node (FastAPI server) and stream logs."""
    try:
        # Check if the FastAPI server is already running
        result = subprocess.run(["pgrep", "-f", SALLMON_SERVER_CMD], stdout=subprocess.PIPE)
        if result.returncode == 0:
            return jsonify({"message": "Node is already running"}), 200

        # Start the server as a subprocess
        process = subprocess.Popen(
            SALLMON_SERVER_CMD.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        def generate_logs():
            """Yield logs from the server."""
            for line in process.stdout:
                yield f"data: {line.strip()}\n\n"
            for line in process.stderr:
                yield f"data: {line.strip()}\n\n"

        return app.response_class(generate_logs(), mimetype="text/event-stream")

    except Exception as e:
        # Ensure we are inside an app context
        with app.app_context():
            return jsonify({"error": str(e)}), 500


@app.route("/start-node-logs", methods=["GET"])
def start_node_logs():
    """Stream logs from the node startup process."""
    try:
        # Check if the FastAPI server is already running
        result = subprocess.run(["pgrep", "-f", SALLMON_SERVER_CMD], stdout=subprocess.PIPE)
        if result.returncode == 0:
            return Response("data: Node is already running\n\n", mimetype="text/event-stream")

        # Start the FastAPI server using sallmon-server command
        process = subprocess.Popen(
            SALLMON_SERVER_CMD.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        def generate_logs():
            """Generator function to yield logs."""
            for line in process.stdout:
                yield f"data: {line.strip()}\n\n"
            for line in process.stderr:
                yield f"data: {line.strip()}\n\n"

        return Response(generate_logs(), mimetype="text/event-stream")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#@app.route("/start-node", methods=["POST"])
#def start_node():
#    """Start the node (FastAPI server)"""
#    try:
        # Check if the FastAPI server is already running
#        result = subprocess.run(["pgrep", "-f", SALLMON_SERVER_CMD], stdout=subprocess.PIPE)
#        if result.returncode == 0:
#            return jsonify({"message": "Node is already running"}), 200
        
        # Start the FastAPI server using sallmon-server command
#        subprocess.Popen(SALLMON_SERVER_CMD.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        return jsonify({"message": "Node started successfully!"}), 200
#    except Exception as e:
#        return jsonify({"error": str(e)}), 500


@app.route("/stop-node", methods=["POST"])
def stop_node():
    """Stop the node (FastAPI server)"""
    try:
        # Find and terminate the FastAPI server process
        result = subprocess.run(["pkill", "-f", SALLMON_SERVER_CMD])
        if result.returncode == 0:
            return jsonify({"message": "Paypal, Stripe and Visa - we are going to eat your lunch!"}), 200
        return jsonify({"error": "Node is not running"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/peers")
def peers():
    """Manage peers"""
    try:
        response = requests.get(f"{BASE_URL}/get-peers")
        peers = response.json().get("peers", [])
        return render_template("peers.html", peers=peers)
    except Exception as e:
        return render_template("peers.html", error=str(e))

@app.route("/mine", methods=["GET", "POST"])
def mine():
    """Mine a new block using a manually entered wallet address."""
    try:
        if request.method == "POST":
            miner_address = request.form.get("miner_address")
            response = requests.post(f"{BASE_URL}/mine-block", json={"miner_address": miner_address})
            if response.status_code == 200:
                block = response.json().get("block")
                return render_template(
                    "mine.html",
                    message="Mining successful!",
                    block=block,
                )
            else:
                error = response.json().get("error", "Failed to mine block.")
                return render_template("mine.html", error=error)
        return render_template("mine.html")
    except Exception as e:
        return render_template("mine.html", error=str(e))


@app.route("/metrics")
def metrics():
    """View node metrics"""
    try:
        response = requests.get(f"{BASE_URL}/metrics")
        metrics = response.json()
        return render_template("metrics.html", metrics=metrics)
    except Exception as e:
        return render_template("metrics.html", error=str(e))



from sallmon.frontend.routes.mining import mining_blueprint
app.register_blueprint(mining_blueprint, url_prefix="/mining")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1338)
