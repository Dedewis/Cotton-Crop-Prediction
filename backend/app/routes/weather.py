from fastapi import APIRouter, Query, HTTPException
from app.services.weather_services import fetch_weather

router = APIRouter()

@router.get("/weather", summary="Get current weather data from Visual Crossing")
def get_weather(
    lat: float = Query(..., description="Latitude (-90 to 90)", ge=-90, le=90),
    lon: float = Query(..., description="Longitude (-180 to 180)", ge=-180, le=180)
):
    """
    Fetches live weather data (temperature, humidity, rainfall)
    from the Visual Crossing API for a given coordinate.
    """
    try:
        weather_data = fetch_weather(lat, lon)
        if not weather_data or all(v is None for v in weather_data.values()):
            raise HTTPException(status_code=502, detail="Failed to fetch weather data from Visual Crossing API")

        return {
            "coordinates": {"lat": lat, "lon": lon},
            "data": weather_data,
            "source": "Visual Crossing Weather API"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather API error: {str(e)}")
