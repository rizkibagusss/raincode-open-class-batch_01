"""HTTP bridge antara frontend dan TransactionService."""

import os

from flask import Flask, jsonify, render_template, request
from mysql.connector import Error

from service import TransactionService

app = Flask(__name__)
service = TransactionService()


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/transactions")
def read_transactions():
    return jsonify(service.get_all())


@app.post("/api/transactions")
def create_transaction():
    try:
        transaction = service.create(request.get_json(silent=True) or {})
        return jsonify(transaction), 201
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@app.patch("/api/transactions/<int:transaction_id>")
def update_transaction(transaction_id: int):
    try:
        transaction = service.update(
            transaction_id,
            request.get_json(silent=True) or {},
        )
        if transaction is None:
            return jsonify({"error": "Transaksi tidak ditemukan."}), 404
        return jsonify(transaction)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@app.delete("/api/transactions/<int:transaction_id>")
def delete_transaction(transaction_id: int):
    if not service.delete(transaction_id):
        return jsonify({"error": "Transaksi tidak ditemukan."}), 404
    return "", 204


@app.errorhandler(Error)
def database_error(error):
    app.logger.error("Database error: %s", error)
    return jsonify({"error": "Database sedang tidak dapat diakses."}), 500


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "True").lower() == "true")
