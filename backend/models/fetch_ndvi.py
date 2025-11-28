from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, bbox_to_dimensions, BBox
import numpy as np
import matplotlib.pyplot as plt

# ====== SET YOUR CREDENTIALS ======
SENTINEL_INSTANCE_ID = "82486eb0-b504-4f33-84ad-0cd975c15aff"
SENTINEL_CLIENT_ID = "6d1a77df-4c3b-47d5-b0d9-97befa09b230" 
SENTINEL_CLIENT_SECRET = "DdGVBh7QSvY7P8v3pBc8majR5skXtSm7"

config = SHConfig()
config.instance_id = SENTINEL_INSTANCE_ID
config.sh_client_id = SENTINEL_CLIENT_ID
config.sh_client_secret = SENTINEL_CLIENT_SECRET

# ====== TEST LOCATION ======
# Example: near Telangana (you can replace these with your coordinates)
latitude = 17.3850
longitude = 78.4867

# Bounding box for ~1km area
bbox = BBox(bbox=[longitude - 0.005, latitude - 0.005, longitude + 0.005, latitude + 0.005], crs="EPSG:4326")
resolution = 60  # meters

# NDVI EVALSCRIPT
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

# Create request
request = SentinelHubRequest(
    data_folder='./data',
    evalscript=evalscript_ndvi,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A,
            time_interval=("2024-07-01", "2024-07-31"),
        )
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.TIFF)
    ],
    bbox=bbox,
    size=bbox_to_dimensions(bbox, resolution=resolution),
    config=config
)

# Fetch data
ndvi_data = request.get_data()[0].squeeze()

# Print average NDVI
average_ndvi = float(np.nanmean(ndvi_data))
print(f"✅ Average NDVI: {average_ndvi:.4f}")

# Optional: visualize
plt.imshow(ndvi_data, cmap='RdYlGn')
plt.colorbar(label="NDVI")
plt.title("NDVI Map")
plt.show()
