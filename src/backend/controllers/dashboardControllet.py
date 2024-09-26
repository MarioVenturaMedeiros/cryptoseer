from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from models.predictionModel import Log  # Assuming the Log model is defined here

# Create a router for log-related routes
router = APIRouter()

# Route to retrieve all logs
def get_logs(db: Session = Depends(get_db)):
    try:
        logs = db.query(Log).all()  # Fetch all logs from the Log table
        if not logs:
            raise HTTPException(status_code=404, detail="No logs found.")
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
