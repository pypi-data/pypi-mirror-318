import os
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from sallmon.frontend.models import Wallet, db
from Crypto.PublicKey import RSA
import hashlib

wallets_bp = Blueprint("wallets", __name__)


@wallets_bp.route("/")
def view_wallets():
    """View all wallets."""
    wallets = Wallet.query.all()  # Query all wallets from the database
    return render_template("wallets.html", wallets=wallets)  # Pass the list of wallets directly to the template

import qrcode

@wallets_bp.route("/new", methods=["GET", "POST"])
def create_wallet():
    """Create a new wallet."""
    if request.method == "POST":
        # Generate wallet keys and address
        key = RSA.generate(2048)
        private_key = key.export_key().decode()
        public_key = key.publickey().export_key().decode()
        address = hashlib.sha256(public_key.encode()).hexdigest()[:34]

        # Add new wallet to the database
        new_wallet = Wallet(
            address=address,
            private_key=private_key,
            public_key=public_key,
            balance=0.0,
        )
        db.session.add(new_wallet)
        db.session.commit()

        # Generate QR Code
        qr = qrcode.make(address)
        os.makedirs("static/assets", exist_ok=True)
        qr.save(f"static/assets/{address}.png")
        wallets = Wallet.query.all()  # Query all wallets from the database

        return redirect(url_for("wallets.view_wallets"))

    return render_template("new_wallet.html")


@wallets_bp.route("/<int:wallet_id>")
def view_wallet(wallet_id):
    """View a single wallet."""
    wallet = Wallet.query.get_or_404(wallet_id)
    return render_template("wallet.html", wallet=wallet)


@wallets_bp.route("/<int:wallet_id>/delete", methods=["POST"])
def delete_wallet(wallet_id):
    """Delete a wallet."""
    wallet = Wallet.query.get_or_404(wallet_id)
    db.session.delete(wallet)
    db.session.commit()
    return jsonify({"message": "Wallet deleted successfully"})
