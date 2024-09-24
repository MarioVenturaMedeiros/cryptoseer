import random
import time
import numpy as np
import pandas as pd
import yfinance as yf
import os
import requests
from models.predictionModel import Model
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models.database import get_db
from prophet import Prophet
import joblib

collection_url = "http://pocketbase:8090/api/collections/{collection_name}/records"

POCKETBASE_URL = "http://pocketbase:8090"

def authenticate_pocketbase():
    try: 
        auth_data = {
            "identity": "teste@gmail.com",
            "password": "testeteste"
        }
        response = requests.post(f"{POCKETBASE_URL}/api/admins/auth-with-password", json=auth_data)

        if response.status_code == 200:
            print("Authenticated successfully!")
            return response.json()["token"]
        else:
            raise HTTPException(status_code=response.status_code, detail="Authentication failed.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
pocketbase_token = authenticate_pocketbase()

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
    # Get the latest model URL from Pocketbase
    model_url = get_model_url()
    
    print("passei 1")
    
    # Generate a unique temporary file name for saving the downloaded model
    unique_filename = f"temp_model_{generate_uuidv7()}.joblib"

    print("passei 1.1")
    
    # Download the model from the URL
    response = requests.get(model_url)
    with open(unique_filename, "wb") as f:
        f.write(response.content)
    
    print("passei 1.2")
    # Load the model using joblib
    model = joblib.load(unique_filename)

    print("passei 1.3")
    
    # Optionally, remove the file after loading the model to clean up the local filesystem
    os.remove(unique_filename)
    
    print("Prophet model loaded successfully from Pocketbase URL.")
    
    return model

def get_model_url(db: Session = Depends(get_db)) -> str:
    # Authenticate and get a token
    
    headers = {
        "Authorization": f"Bearer {pocketbase_token}"
    }

    collection_name = "models"  # Assuming you have a collection named "models"
    request_url = f"http://pocketbase:8090/api/collections/{collection_name}/records"
    
    try:
        # Request to fetch the latest record, sorted by creation time
        response = requests.get(request_url, headers=headers, params={"sort": "-created", "perPage": 1})
        response.raise_for_status()
        
        # Parse the response to get the URL of the latest model
        latest_record = response.json()["items"][0]
        file_id = latest_record["id"]  # Record ID
        file_list = latest_record.get("field", [])  # The field that holds the file(s)
        
        # Extract the file name from the list (assuming it's a list)
        if isinstance(file_list, list) and file_list:
            file_name = file_list[0]  # Get the first file from the list
        else:
            raise Exception("No file found in the field")
        
        # Generate the URL for the file using PocketBase's file API
        model_url = f"http://pocketbase:8090/api/files/{latest_record['collectionId']}/{file_id}/{file_name}"
        
        print(f"Latest model URL fetched: {model_url}")
        return model_url
    
    except requests.RequestException as e:
        raise Exception(f"Error fetching the latest model URL: {e}")
    
def fetch_latest_dogecoin_data():
    """Fetch and prepare the latest Dogecoin data for prediction using Yfinance."""
    # Fetch Dogecoin data using yfinance
    doge_ticker = yf.Ticker("DOGE-USD")
    df = doge_ticker.history(period="1d", interval="1d")

    # If no data is returned, raise an error
    if df.empty:
        raise ValueError("No data fetched for Dogecoin (DOGE-USD)")

    # Extract the last known values and format it into a dictionary
    last_row = df.tail(1)

    # Prepare a dictionary with the latest values, formatted for Prophet
    latest_data = {
        'ds': last_row.index[0],  # Date
        'Open': last_row['Open'].values[0],
        'High': last_row['High'].values[0],
        'Low': last_row['Low'].values[0],
        'Volume': last_row['Volume'].values[0]
    }

    return latest_data