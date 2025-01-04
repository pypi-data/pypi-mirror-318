from flask import Blueprint, render_template, request, jsonify
import requests

BASE_URL = "http://127.0.0.1:1337"

node_bp = Blueprint('node', __name__)

@node_bp.route('/')
def node_home():
    """Node home page."""
    return render_template('home.html')

@node_bp.route('/start', methods=['POST'])
def start_node():
    """Start the node."""
    try:
        response = requests.post(f"{BASE_URL}/start-node")
        if response.status_code == 200:
            return jsonify({"message": "Node started successfully!"})
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@node_bp.route('/stop', methods=['POST'])
def stop_node():
    """Stop the node."""
    try:
        response = requests.post(f"{BASE_URL}/stop-node")
        if response.status_code == 200:
            return jsonify({"message": "Node stopped successfully!"})
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
