import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)


def clean_number(value: str):
    """Convert '1,23,456.78' → 123456.78, returns None if empty"""
    if not value or value.strip() == "":
        return None
    try:
        return float(value.replace(",", "").strip())
    except ValueError:
        return None


def insert_invoice(bill_data: dict):
    """
    Cleans and inserts parsed invoice data into Supabase.

    Args:
        bill_data (dict): The dictionary returned by parse_bill_data()

    Returns:
        dict: The inserted row from Supabase
    """

    payload = {
        # Required - text fields
        "invoice_number":   bill_data.get("invoice_number"),
        "invoice_date":     bill_data.get("invoice_date"),
        "seller_name":      bill_data.get("seller_name"),
        "seller_gstin":     bill_data.get("seller_gstin"),
        "buyer_name":       bill_data.get("buyer_name"),
        "description":      bill_data.get("description"),

        # Required - numeric fields
        "taxable_amount":   clean_number(bill_data.get("taxable_amount")),
        "invoice_total":    clean_number(bill_data.get("invoice_total")),

        # Optional - text fields
        "buyer_gstin":      bill_data.get("buyer_gstin") or None,
        "hsn_code":         bill_data.get("hsn_code") or None,
        "unit":             bill_data.get("unit") or None,
        "eway_bill_number": bill_data.get("eway_bill_number") or None,
        "vehicle_number":   bill_data.get("vehicle_number") or None,
        "dispatch_location":bill_data.get("dispatch_location") or None,
        "amount_in_words":  bill_data.get("amount_in_words") or None,

        # Optional - numeric fields
        "quantity":         clean_number(bill_data.get("quantity")),
        "rate":             clean_number(bill_data.get("rate")),
        "cgst_rate":        clean_number(bill_data.get("cgst_rate")),
        "cgst_amount":      clean_number(bill_data.get("cgst_amount")),
        "sgst_rate":        clean_number(bill_data.get("sgst_rate")),
        "sgst_amount":      clean_number(bill_data.get("sgst_amount")),
        "igst_rate":        clean_number(bill_data.get("igst_rate")),
        "igst_amount":      clean_number(bill_data.get("igst_amount")),
        "cess_rate":        clean_number(bill_data.get("cess_rate")),
        "cess_amount":      clean_number(bill_data.get("cess_amount")),
        "tcs_rate":         clean_number(bill_data.get("tcs_rate")),
        "tcs_amount":       clean_number(bill_data.get("tcs_amount")),
    }

    response = supabase.table("invoices").insert(payload).execute()
    return response.data