import random
import time
import numpy as np
import pandas as pd
import os
import requests
from models.predictionModel import Model
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models.database import get_db
from prophet import Prophet
import joblib


def analyze_predictions(predictions: pd.DataFrame) -> dict:
    yhat_values = predictions['yhat'].values
    lowest_value = yhat_values.min()
    highest_value = yhat_values.max()
    
    # Get the days corresponding to the lowest and highest values
    lowest_day = predictions[predictions['yhat'] == lowest_value]['ds'].values[0]
    highest_day = predictions[predictions['yhat'] == highest_value]['ds'].values[0]
    
    return {
        "lowest_value": lowest_value,
        "highest_value": highest_value,
        "lowest_day": lowest_day,
        "highest_day": highest_day
    }

def generate_uuidv7():
    timestamp_ms = int(time.time() * 1000)
    time_hex = f'{timestamp_ms:x}'
    random_hex = ''.join([f'{random.randint(0, 15):x}' for _ in range(26)])
    uuidv7 = f'{time_hex[:8]}-{time_hex[8:12]}-7{time_hex[12:15]}-{random_hex[:4]}-{random_hex[4:]}'
    return uuidv7

def load_prophet_model() -> Prophet:
    # Static URL where the Prophet model is stored
    model_url = "http://pocketbase:8090/api/files/4forqd5s2ez9ydw/wwpjocvw1obr90r/modelo_0cJQGhMAmk.joblib"
    
    # Generate a unique temporary file name for saving the downloaded model
    unique_filename = f"temp_model_{generate_uuidv7()}.joblib"
    
    # Download the model from the URL
    response = requests.get(model_url)
    with open(unique_filename, "wb") as f:
        f.write(response.content)
    
    # Load the model using joblib
    model = joblib.load(unique_filename)
    
    # Optionally, remove the file after loading the model to clean up the local filesystem
    os.remove(unique_filename)
    
    print("Prophet model loaded successfully from URL.")
    
    return model



def get_model_url(ID_modelo: str, db: Session = Depends(get_db)) -> str:
    # Query the Model table to find the record with the given ID_modelo
    record = db.query(Model).filter(Model.ID_modelo == ID_modelo).first()

    if not record:
        raise HTTPException(status_code=404, detail="Model not found")

    # Accessing the actual string value
    url_modelo = record.URL_modelo

    return url_modelo