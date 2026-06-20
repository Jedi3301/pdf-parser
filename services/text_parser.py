import re

REQUIRED_KEYS = [
    "invoice_number",
    "invoice_date",
    "seller_name",
    "seller_gstin",
    "buyer_name",
    "description",
    "taxable_amount",
    "invoice_total",
]

OPTIONAL_KEYS = [
    "buyer_gstin",
    "hsn_code",
    "quantity",
    "unit",
    "rate",
    "cgst_rate",
    "cgst_amount",
    "sgst_rate",
    "sgst_amount",
    "igst_rate",
    "igst_amount",
    "cess_rate",
    "cess_amount",
    "tcs_rate",
    "tcs_amount",
    "eway_bill_number",
    "vehicle_number",
    "dispatch_location",
    "amount_in_words",
]


def parse_bill_data(text_pages):
    full_text = "\n".join(text_pages)

    bill_data = {key: "" for key in REQUIRED_KEYS + OPTIONAL_KEYS}

    # Invoice Number
    m = re.search(r'(?:Invoice No|Invoice Number|Inv No)[:\s]*([A-Za-z0-9-/]+)', full_text, re.IGNORECASE)
    if m: bill_data['invoice_number'] = m.group(1).strip()

    # Invoice Date
    m = re.search(r'(?:Invoice Date|Inv Date)[:\s]*(\d{2}[-/]\d{2}[-/]\d{4}|\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4})', full_text, re.IGNORECASE)
    if m: bill_data['invoice_date'] = m.group(1).strip()

    # Seller Name
    m = re.search(r'(?:Seller Name|Sold By|From)[:\s]*(.*?)(?:\n)', full_text, re.IGNORECASE)
    if m: bill_data['seller_name'] = m.group(1).strip()

    # Seller GSTIN
    m = re.search(r'(?:Seller GSTIN|Our GSTIN|GSTIN No)[:\s]*([0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1})', full_text, re.IGNORECASE)
    if m: bill_data['seller_gstin'] = m.group(1).strip()

    # Buyer Name
    m = re.search(r'(?:Buyer Name|Buyer|Bill To|Consignee)[:\s]*(.*?)(?:\n)', full_text, re.IGNORECASE)
    if m: bill_data['buyer_name'] = m.group(1).strip()

    # Buyer GSTIN
    m = re.search(r'(?:Buyer GSTIN|Party GSTIN|GSTIN)[:\s]*([0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1})', full_text, re.IGNORECASE)
    if m: bill_data['buyer_gstin'] = m.group(1).strip()

    # Description
    m = re.search(r'(?:Description of Goods|Description)[:\s]*(.*?)(?:\n|HSN)', full_text, re.IGNORECASE | re.DOTALL)
    if m: bill_data['description'] = m.group(1).strip()

    # HSN Code
    m = re.search(r'(?:HSN/SAC|HSN Code|HSN)[:\s]*([0-9]{4,8})', full_text, re.IGNORECASE)
    if m: bill_data['hsn_code'] = m.group(1).strip()

    # Quantity
    m = re.search(r'(?:Quantity|Qty)[:\s]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['quantity'] = m.group(1).strip()

    # Unit
    m = re.search(r'(?:Unit|Per|UOM)[:\s]*([A-Za-z]+)', full_text, re.IGNORECASE)
    if m: bill_data['unit'] = m.group(1).strip()

    # Rate
    m = re.search(r'(?:Rate\s*\(PMT\)|Rate)[:\s]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['rate'] = m.group(1).strip()

    # Taxable Amount
    m = re.search(r'(?:Taxable Amount|Taxable Value|Amount\s*\(Rs\.\))[:\s]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['taxable_amount'] = m.group(1).strip()

    # CGST Rate
    m = re.search(r'(?:CGST\s*@\s*)([\d.]+)%', full_text, re.IGNORECASE)
    if m: bill_data['cgst_rate'] = m.group(1).strip()

    # CGST Amount
    m = re.search(r'(?:CGST)[:\s*@\d.%]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['cgst_amount'] = m.group(1).strip()

    # SGST Rate
    m = re.search(r'(?:SGST\s*@\s*)([\d.]+)%', full_text, re.IGNORECASE)
    if m: bill_data['sgst_rate'] = m.group(1).strip()

    # SGST Amount
    m = re.search(r'(?:SGST)[:\s*@\d.%]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['sgst_amount'] = m.group(1).strip()

    # IGST Rate
    m = re.search(r'(?:IGST\s*@\s*)([\d.]+)%', full_text, re.IGNORECASE)
    if m: bill_data['igst_rate'] = m.group(1).strip()

    # IGST Amount
    m = re.search(r'(?:IGST)[:\s*@\d.%]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['igst_amount'] = m.group(1).strip()

    # Cess Rate
    m = re.search(r'(?:Compensation Cess|Cess)\s*@\s*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['cess_rate'] = m.group(1).strip()

    # Cess Amount
    m = re.search(r'(?:Compensation Cess\s*\(PMT\)|OUTPUT COMPENSATION CESS[^:]*)[:\s]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['cess_amount'] = m.group(1).strip()

    # TCS Rate
    m = re.search(r'(?:TCS\s*@\s*)([\d.]+)%', full_text, re.IGNORECASE)
    if m: bill_data['tcs_rate'] = m.group(1).strip()

    # TCS Amount
    m = re.search(r'(?:TCS Payable Amount|TCS)[:\s*@\d.%]*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['tcs_amount'] = m.group(1).strip()

    # Invoice Total
    m = re.search(r'(?:Total Invoice Amount|Total Amount|Grand Total)[:\s]*Rs\.?\s*([\d,.]+)', full_text, re.IGNORECASE)
    if m: bill_data['invoice_total'] = m.group(1).strip()

    # E-Way Bill Number
    m = re.search(r'(?:E-Way Bill No|E-Way Bill Number)[:\s]*(\d{12})', full_text, re.IGNORECASE)
    if m: bill_data['eway_bill_number'] = m.group(1).strip()

    # Vehicle Number
    m = re.search(r'(?:Truck No|Motor Vehicle No|Vehicle No)[:\s]*([A-Z]{2}[\s-]?\d{2}[\s-]?[A-Z]{1,2}[\s-]?\d{4})', full_text, re.IGNORECASE)
    if m: bill_data['vehicle_number'] = m.group(1).strip()

    # Dispatch Location
    m = re.search(r'(?:Despatch From|Dispatch From)[:\s]*(.*?)(?:\n|GSTIN)', full_text, re.IGNORECASE | re.DOTALL)
    if m: bill_data['dispatch_location'] = m.group(1).strip()

    # Amount in Words
    m = re.search(r'(?:Amount In Words|Amount Chargeable\s*\(in words\)|Rupees In Words)[:\s]*(.*?)(?:\n|$)', full_text, re.IGNORECASE)
    if m: bill_data['amount_in_words'] = m.group(1).strip()

    # Validation
    missing = [key for key in REQUIRED_KEYS if not bill_data.get(key)]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    return bill_data

    
