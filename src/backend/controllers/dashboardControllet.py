from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.database import get_db
from models.predictionModel import Log  # Assuming the Log model is defined here
import yfinance as yf
import io
import pandas as pd
import base64
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

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
    
def plot_observed(data):
    plt.figure(figsize=(10, 4))
    data.plot(title='Observado')
    plt.xlabel('Date')
    plt.ylabel('Price')
    buf = save_plot_to_buffer()
    return buf

def plot_trend(data):
    decomposition = seasonal_decompose(data, model='multiplicative', period=30)
    plt.figure(figsize=(10, 4))
    decomposition.trend.plot(title='Tendência')
    plt.xlabel('Date')
    plt.ylabel('Trend')
    buf = save_plot_to_buffer()
    return buf

def plot_seasonality(data):
    decomposition = seasonal_decompose(data, model='multiplicative', period=30)
    plt.figure(figsize=(10, 4))
    decomposition.seasonal.plot(title='Sazonalidade')
    plt.xlabel('Date')
    plt.ylabel('Seasonality')
    buf = save_plot_to_buffer()
    return buf

def plot_residual(data):
    decomposition = seasonal_decompose(data, model='multiplicative', period=30)
    plt.figure(figsize=(10, 4))
    decomposition.resid.plot(title='Ruído')
    plt.xlabel('Date')
    plt.ylabel('Residuals')
    buf = save_plot_to_buffer()
    return buf

def save_plot_to_buffer():
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

def plot_decomposition(data):
    decomposition = seasonal_decompose(data, model='multiplicative', period=30)
    
    observed_img = plot_component(decomposition.observed, 'Observado')
    trend_img = plot_component(decomposition.trend, 'Tendência')
    seasonal_img = plot_component(decomposition.seasonal, 'Sazonalidade')
    residual_img = plot_component(decomposition.resid, 'Ruído')

    return observed_img, trend_img, seasonal_img, residual_img

def plot_component(component, title):
    plt.figure(figsize=(10, 4))
    component.plot(title=title)
    plt.xlabel('Date')
    plt.ylabel(title)
    return save_plot_to_buffer()

async def get_dogecoin_data():
    dogecoin = yf.Ticker("DOGE-USD")
    dogecoin_data = dogecoin.history(period="5y")

    # Get 2-year data
    dogecoin2y = dogecoin.history(period="2y")

    # Decomposition for 2-year data
    observed_img, trend_img, seasonal_img, residual_img = plot_decomposition(dogecoin2y['Close'])

    return JSONResponse(content={
        "observed": observed_img,
        "trend": trend_img,
        "seasonal": seasonal_img,
        "residual": residual_img,
        "data": dogecoin_data['Close'].tolist(),  # Send 5-year data for other visualizations
        "data_2y": dogecoin2y['Close'].tolist()    # Send 2-year data for additional use
    })
