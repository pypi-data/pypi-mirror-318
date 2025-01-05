from flask import Blueprint, jsonify
import requests

BASE_URL = "http://127.0.0.1:1337"  # Replace with your backend API

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/", methods=["GET"])
def metrics_home():
    """Metrics home page"""
    try:
        response = requests.get(f"{BASE_URL}/metrics")
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@metrics_bp.route("/blockchain", methods=["GET"])
def get_blockchain():
    """Fetch the entire blockchain"""
    try:
        response = requests.get(f"{BASE_URL}/blocks")
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@metrics_bp.route("/sync-status", methods=["GET"])
def get_sync_status():
    """Fetch the sync status of the node"""
    try:
        response = requests.get(f"{BASE_URL}/sync-status")
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@metrics_bp.route("/node-stats", methods=["GET"])
def get_node_stats():
    """Fetch node statistics"""
    try:
        response = requests.get(f"{BASE_URL}/node-stats")
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
