from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import PlainTextResponse
from services.text_extracter import extract_text_from_pdf

router = APIRouter()


@router.post("/parse", response_class=PlainTextResponse)
async def parse_invoice(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")

    pdf_bytes = await file.read()
    raw_text = extract_text_from_pdf(pdf_bytes)
    
    return raw_text
