from services.text_extracter import extract_text_from_pdf
from services.text_parser import parse_bill_data
from services.db import insert_invoice

# 1. Extract
text_pages = extract_text_from_pdf("path/to/bill.pdf")

# 2. Parse
bill_data = parse_bill_data(text_pages)

# 3. Insert
inserted = insert_invoice(bill_data)
print(inserted)