from flask import Blueprint, render_template, request, jsonify
import requests

BASE_URL = "http://127.0.0.1:1337"

peers_bp = Blueprint('peers', __name__)

@peers_bp.route('/')
def peers():
    """List peers."""
    try:
        response = requests.get(f"{BASE_URL}/get-peers")
        peers = response.json().get("peers", [])
        return render_template('peers.html', peers=peers)
    except Exception as e:
        return f"Error: {str(e)}", 500

@peers_bp.route('/add', methods=['POST'])
def add_peer():
    """Add a peer."""
    peer_ip = request.form.get('peer_ip')
    if not peer_ip:
        return jsonify({"error": "Peer IP is required"}), 400
    try:
        response = requests.post(f"{BASE_URL}/register-peer", json={"ip": peer_ip})
        if response.status_code == 200:
            return jsonify({"message": f"Peer {peer_ip} registered successfully!"})
        return jsonify({"error": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
