import re

def parse_bill_data(text_pages):
    """
    Parses the extracted text from PDF pages to find specific billing information.

    Args:
        text_pages (list): A list of strings, where each string is the text from a page.

    Returns:
        dict: A dictionary containing the extracted key-value pairs.
    """
    bill_data = {}
    full_text = "\\n".join(text_pages)

    # Example extractions - you will need to add more patterns for all your fields
    
    # Invoice No
    invoice_no_match = re.search(r'(?:Invoice No|Inv No|Invoice Number)[:\s]*([A-Za-z0-9-/]+)', full_text, re.IGNORECASE)
    if invoice_no_match:
        bill_data['Invoice No'] = invoice_no_match.group(1).strip()

    # Invoice Date
    invoice_date_match = re.search(r'(?:Invoice Date|Date)[:\s]*(\d{2}[-/]\d{2}[-/]\d{4}|\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4})', full_text, re.IGNORECASE)
    if invoice_date_match:
        bill_data['Invoice Date'] = invoice_date_match.group(1).strip()

    # Total Invoice Amount
    total_invoice_amount_match = re.search(r'(?:Total Invoice Amount|Total Amount|Grand Total)[:\s]*Rs\.?\s*([\d,\.]+)', full_text, re.IGNORECASE)
    if total_invoice_amount_match:
        bill_data['Total Invoice Amount'] = total_invoice_amount_match.group(1).strip()
        
    # Amount In Words
    amount_in_words_match = re.search(r'(?:Amount In Words|Rupees In Words)[:\s]*(.*?)(?:\n|$)', full_text, re.IGNORECASE)
    if amount_in_words_match:
        bill_data['Amount In Words'] = amount_in_words_match.group(1).strip()

    # HSN Code
    hsn_code_match = re.search(r'(?:HSN Code|HSN)[:\s]*([0-9A-Z]+)', full_text, re.IGNORECASE)
    if hsn_code_match:
        bill_data['HSN Code'] = hsn_code_match.group(1).strip()
        
    # GSTIN No
    gstin_no_match = re.search(r'(?:GSTIN No|GSTIN)[:\s]*([0-9A-Z]{15})', full_text, re.IGNORECASE)
    if gstin_no_match:
        bill_data['GSTIN No'] = gstin_no_match.group(1).strip()
        
    # E-Way Bill No
    e_way_bill_no_match = re.search(r'(?:E-Way Bill No|E-Way Bill)[:\s]*(\d{12})', full_text, re.IGNORECASE)
    if e_way_bill_no_match:
        bill_data['E-Way Bill No'] = e_way_bill_no_match.group(1).strip()
    
    # Truck No
    truck_no_match = re.search(r'(?:Truck No|Motor Vehicle No)[:\s]*([A-Z0-9\s-]+)', full_text, re.IGNORECASE)
    if truck_no_match:
        bill_data['Truck No'] = truck_no_match.group(1).strip()
        
    # Despatch From
    despatch_from_match = re.search(r'(?:Despatch From|Dispatch From)[:\s]*(.*?)(?:\n|GSTIN)', full_text, re.IGNORECASE | re.DOTALL)
    if despatch_from_match:
        bill_data['Despatch From'] = despatch_from_match.group(1).strip()
        
    # Reference No. & Date
    reference_no_date_match = re.search(r'(?:Reference No\.? & Date)[:\s]*([A-Za-z0-9-/,\s]+)', full_text, re.IGNORECASE)
    if reference_no_date_match:
        bill_data['Reference No. & Date'] = reference_no_date_match.group(1).strip()

    # You will need to add more regex patterns for other fields like:
    # Description
    # Vessel
    # Date (for Page 2)
    # Weight (MT)
    # Rate (PMT)
    # Amount (Rs.)
    # Total (for general sections)
    # CGST
    # SGST
    # Compensation Cess (PMT)
    # TCS Payable Amount
    # Total Amount (general)
    # OUTPUT TAX CGST @ 2.5%
    # OUTPUT TAX SGST @ 2.5%
    # OUTPUT COMPENSATION CESS @ RS.400/MT
    # TCS @1%
    # Total (for Page 2)
    # Amount Chargeable (in words) (for Page 2)
    
    return bill_data