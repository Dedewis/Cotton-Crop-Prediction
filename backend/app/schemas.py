from pydantic import BaseModel

class InputData(BaseModel):
    
    temperature: float
    rainfall: float
    humidity: float
    

class PredictionResult(BaseModel):
    suitability_score: float
    market_score: float
    final_score: float
    recommendation: str
    crop_yield:float
