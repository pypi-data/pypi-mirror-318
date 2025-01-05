from flask import Blueprint, jsonify

blocks_bp = Blueprint("blocks", __name__)

@blocks_bp.route("/blocks", methods=["GET"])
def get_blocks():
    return jsonify({"message": "Blocks endpoint is working!"})
