from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.auth import admin_required
from app.database import SessionLocal
from app.models.log import LogEntry

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/logs")
def get_logs(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    _: str = Depends(admin_required)  # Enforces admin-only access
):
    logs = db.query(LogEntry).order_by(LogEntry.timestamp.desc()).offset(offset).limit(limit).all()
    return logs
