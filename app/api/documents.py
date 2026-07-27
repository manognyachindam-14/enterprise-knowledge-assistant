from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate


router = APIRouter()


@router.post("/documents")
def create_document(
    document_data: DocumentCreate,
    db: Session = Depends(get_db),
):
    document = Document(
        filename=document_data.filename
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document
    