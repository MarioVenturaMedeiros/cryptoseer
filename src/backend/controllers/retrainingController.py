from fastapi import UploadFile, Depends, HTTPException
import pandas as pd
import numpy as np
from utils.helpers import authenticate_pocketbase
import requests
import os
import yfinance as yf
from prophet import Prophet
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
import joblib
import tempfile

# PocketBase configuration
pocketbase_token = authenticate_pocketbase()

def upload_to_pocketbase(file_path, pocketbase_token):
    try:
        url = "http://pocketbase:8090/api/collections/models/records"

        # Use the correct field name from Pocketbase ('field')
        files = {'field': open(file_path, 'rb')}  # 'field' matches the name in your Pocketbase setup
        headers = {
            'Authorization': f'Bearer {pocketbase_token}'
        }

        response = requests.post(url, files=files, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error uploading file: {response.status_code}")
            print(f"Response content: {response.content}")
            return False
    except Exception as e:
        print(f"Exception during file upload: {e}")
        return False

def retraining():
    try:
        # Fetch DOGE-USD data
        dogecoin = yf.Ticker('DOGE-USD')
        dogecoin = dogecoin.history(period="2y")
        dogecoin_reset = dogecoin.reset_index()

        # Rename columns for Prophet
        dogecoin_prophet = dogecoin_reset[['Date', 'Close', 'Open', 'High', 'Low', 'Volume']].rename(columns={'Date': 'ds', 'Close': 'y'})
        
        # Remove timezone if present in 'ds'
        dogecoin_prophet['ds'] = pd.to_datetime(dogecoin_prophet['ds']).dt.tz_localize(None)

        tscv = TimeSeriesSplit(n_splits=5)

        # Iterate over the train-test splits
        for train_index, test_index in tscv.split(dogecoin_prophet):
            train_df, test_df = dogecoin_prophet.iloc[train_index], dogecoin_prophet.iloc[test_index]
            
            # Initialize a new Prophet model for each fold
            model = Prophet()
            
            # Add the regressors
            model.add_regressor('Open')
            model.add_regressor('High')
            model.add_regressor('Low')
            model.add_regressor('Volume')
            
            # Train the model on the train set
            print(f"Training model on fold with {len(train_df)} training samples and {len(test_df)} test samples")
            model.fit(train_df)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".joblib") as tmp_file:
            model_file_path = tmp_file.name
            # Save the multivariate Prophet model to the temporary file
            joblib.dump(model, model_file_path)

        # Check if the file was saved correctly by printing its size
        file_size = os.path.getsize(model_file_path)
        print(f"Model file size before upload: {file_size} bytes")

        if file_size == 0:
            print("The model file was not saved correctly.")
            return False

        # Upload the model file to Pocketbase
        upload_response = upload_to_pocketbase(model_file_path, pocketbase_token)
        
        # Print the upload response for debugging
        print(f"Upload response: {upload_response}")
        
        if not upload_response:
            print("Failed to upload file to Pocketbase.")
            return False

        # Inspect the actual response structure to check for the correct key
        # Adjust the check based on the real structure of the response
        if 'field' in upload_response:  # Adjust this key based on the actual response
            print(f"File uploaded successfully with metadata: {upload_response['field']}")
        else:
            print("No file metadata found in the Pocketbase response.")
            return False

        return True

    except Exception as e:
        print(f"Exception during retraining: {e}")
        return False

    finally:
        # Remove the temporary file after upload
        if os.path.exists(model_file_path):
            os.remove(model_file_path)
            print(f"Temporary file {model_file_path} removed.")

