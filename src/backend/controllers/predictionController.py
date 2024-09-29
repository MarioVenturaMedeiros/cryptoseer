from fastapi import UploadFile, Depends, HTTPException
import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from models.database import get_db
from utils.helpers import analyze_predictions, generate_uuidv7, load_prophet_model, fetch_latest_dogecoin_data, authenticate_pocketbase
from typing import List
import requests
import os
import yfinance as yf

# PocketBase configuration

pocketbase_token = authenticate_pocketbase()
# Initialize PocketBase authentication (you can save this token for further requests)


def predict(db: Session = Depends(get_db)) -> dict:
    try:
        # Load the latest Prophet model from Pocketbase
        model = load_prophet_model()

        print("passei 2")

        # Fetch and format the latest available Dogecoin data from Yfinance
        latest_data = fetch_latest_dogecoin_data()

        # Create a dataframe with future dates (10 days ahead)
        future = model.make_future_dataframe(periods=10)
        print(f"passei 3 - Future dataframe created:\n{future.head()}")  # Check the future dataframe

        # Add the regressors (Open, High, Low, Volume) from the latest Dogecoin data
        future['Open'] = latest_data['Open']
        future['High'] = latest_data['High']
        future['Low'] = latest_data['Low']
        future['Volume'] = latest_data['Volume']

        print(f"Future dataframe with added regressors:\n{future.head()}")

        # Predict the next 10 days using Prophet
        forecast = model.predict(future)
        print(f"passei 4 - Forecast generated:\n{forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()}")

        # Select only the last 10 days from the forecast
        future_forecast = forecast[['ds', 'yhat']].tail(10)

        # Convert 'ds' from numpy.datetime64 to Python datetime for serialization
        future_forecast['ds'] = future_forecast['ds'].apply(lambda x: x.to_pydatetime() if isinstance(x, (pd.Timestamp, np.datetime64)) else x)

        # Analyze the forecasted data (find highest and lowest predicted values)
        analysis = analyze_predictions(future_forecast)

        print("passei 5")
        
        # Return the forecasted values and the analysis (lowest and highest value)
        return {
            "predicted_values": future_forecast.to_dict(orient="records"),
            "lowest_value": analysis["lowest_value"],
            "highest_value": analysis["highest_value"],
            # "lowest_day": analysis["lowest_day"],
            # "highest_day": analysis["highest_day"]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
