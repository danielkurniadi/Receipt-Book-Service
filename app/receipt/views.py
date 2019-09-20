from flask import Blueprint, jsonify, request

from app.receipt.libs import (
    receipt_manager,
)

mod_receipt = Blueprint('receipt', __name__)


# ------------------------
# RECEIPT FILE
# ------------------------

@mod_receipt.route('/api/receipts/summary', methods=['POST'])
def api_receipt_summary():
    imgstream = request.files['file'].stream
    error, summary = receipt_manager.summarize_receipt_file(imgstream)

    return jsonify({
        **error.to_json(),
        'data': summary,
    }), error.http_status
