from fastapi import APIRouter, UploadFile, File, HTTPException
from services.text_extracter import extract_text_from_pdf
from services.text_parser import parse_bill_data

router = APIRouter()


@router.post("/parse")
async def parse_invoice(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")

    pdf_bytes = await file.read()
    text_pages = extract_text_from_pdf(pdf_bytes)
    result = parse_bill_data(text_pages)
    return result
