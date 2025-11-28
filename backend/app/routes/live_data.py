from fastapi import APIRouter, Query
from app.utils import fetch_live_cotton_price, fetch_local_cotton_price

router = APIRouter()

@router.get("/cotton")
def get_cotton_data(
    state: str = Query(None),
    district: str = Query(None),
    commodity: str = Query(None),
    date: str = Query(None),
    source: str = Query("api", description="Choose 'api' or 'csv'")
):
    """
    Get cotton mandi data.
    - source = 'api' → fetch from live API
    - source = 'csv' → fetch from local CSV
    """
    if source == "csv":
        return fetch_local_cotton_price(state, district, commodity, date)
    else:
        return fetch_live_cotton_price(state, district, commodity, date)
