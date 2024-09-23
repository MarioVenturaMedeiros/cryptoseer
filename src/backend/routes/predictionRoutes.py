from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from controllers.predictionController import (root, mock_data, predict)
from models.database import get_db

router = APIRouter()

router.get("/")(root)
router.post("/mock")(mock_data)
router.post("/predict")(predict)
