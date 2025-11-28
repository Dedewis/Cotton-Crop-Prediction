from fastapi import APIRouter, HTTPException, Query
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, bbox_to_dimensions, BBox
import numpy as np
import os

router = APIRouter()

# Sentinel Hub credentials from environment variables
INSTANCE_ID = os.getenv("SENTINEL_INSTANCE_ID")
CLIENT_ID = os.getenv("SENTINEL_CLIENT_ID")
CLIENT_SECRET = os.getenv("SENTINEL_CLIENT_SECRET")

# Configure Sentinel Hub
config = SHConfig()
config.instance_id = INSTANCE_ID
config.sh_client_id = CLIENT_ID
config.sh_client_secret = CLIENT_SECRET

@router.get("/get-ndvi")
def get_ndvi(lat: float = Query(...), lon: float = Query(...)):
    """
    Fetch NDVI value for a given latitude and longitude using Sentinel Hub.
    """
    try:
        bbox = BBox(
            bbox=[lon - 0.005, lat - 0.005, lon + 0.005, lat + 0.005],
            crs="EPSG:4326"
        )
        resolution = 60

        evalscript_ndvi = """
        //VERSION=3
        function setup() {
          return {
            input: ["B04", "B08"],
            output: { bands: 1, sampleType: "FLOAT32" }
          };
        }
        function evaluatePixel(sample) {
          let ndvi = (sample.B08 - sample.B04) / (sample.B08 + sample.B04);
          return [ndvi];
        }
        """

        request = SentinelHubRequest(
            data_folder='./data',
            evalscript=evalscript_ndvi,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L2A,
                    time_interval=("2024-07-01", "2024-07-31"),
                )
            ],
            responses=[SentinelHubRequest.output_response('default', MimeType.TIFF)],
            bbox=bbox,
            size=bbox_to_dimensions(bbox, resolution=resolution),
            config=config
        )

        ndvi_data = request.get_data()[0].squeeze()
        avg_ndvi = float(np.nanmean(ndvi_data))

        return {
            "latitude": lat,
            "longitude": lon,
            "average_ndvi": avg_ndvi
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
