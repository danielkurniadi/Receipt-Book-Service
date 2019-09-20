from app.parser.ocr_receipt_parser import ocr_parse_image_to_text
from app.parser.text_receipt_parser import (
    parse_market_in_text,
    parse_sum_in_text
)

from app.bridges.errors import ServerOk, Error

# ------------------------
# MANAGER HELPER
# ------------------------

def __check_user_owns_receipt(user_id, receipt_id):
    user_receipt_ids = receipt_model_manager.get_user_receipts(user_id)
    return receipt_id in user_receipt_ids


# ------------------------
# LEVEL PUBLIC
# ------------------------

def summarize_receipt_file(img_stream):
    extracted_text = ocr_parse_image_to_text(img_stream)
    if not extracted_text:
        return ServerOk, {}
    total_sum = parse_sum_in_text(extracted_text)
    market = parse_market_in_text(extracted_text)
    date = "12-09-2018"
    receipt_summary = {
        'totalSum': total_sum,
        'market': market,
        'date': date
    }
    return ServerOk(), receipt_summary

