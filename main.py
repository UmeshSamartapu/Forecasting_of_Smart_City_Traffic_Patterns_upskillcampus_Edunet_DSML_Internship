from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
import pickle
import numpy as np
import os
import urllib.request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Initialize FastAPI app
app = FastAPI()

# Path to model
MODEL_PATH = "traffic_forecasting_model.pkl"
MODEL_URL = "https://huggingface.co/UmeshSamartapu/NewProject/resolve/main/traffic_forecasting_model.pkl"

# Download model if not found
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Hugging Face...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# Load model
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

# Setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the input structure
class TrafficInput(BaseModel):
    junction: int
    hour: int
    day_of_week: int
    is_weekend: int
    month: int

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict")
async def predict(
    request: Request,
    Junction: int = Form(...),
    Hour: int = Form(...),
    DayOfWeek: int = Form(...),
    IsWeekend: int = Form(...),
    Month: int = Form(...)
):
    # Prepare the input data
    input_data = np.array([[Junction, Hour, DayOfWeek, IsWeekend, Month]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return template with prediction
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": int(prediction[0])
    })
