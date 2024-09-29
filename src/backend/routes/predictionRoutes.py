from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from controllers.predictionController import (predict)
from models.database import get_db
from controllers.retrainingController import (retraining)
from controllers.dashboardControllet import (get_logs, get_dogecoin_data)

router = APIRouter()

router.post("/predict")(predict)
router.get("/retraining")(retraining)
router.get("/logs")(get_logs)
router.get("/dogecoin")(get_dogecoin_data)
