from fastapi import FastAPI
from app.routes import predict, live_data, ndvi, weather



app = FastAPI(
    title="Cotton Crop Prediction API",
    description="Backend API for price prediction, NDVI analysis, and environmental suitability.",
    version="1.0.0",
)

# Existing prediction endpoint
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])

# New live cotton price endpoint
app.include_router(live_data.router, tags=["Live Data"])

app.include_router(ndvi.router, prefix="/live", tags=["NDVI"])

app.include_router(weather.router, tags=["Weather"])

@app.get("/")
def root():
    return {"message": "Cotton Crop Prediction API is running"}
