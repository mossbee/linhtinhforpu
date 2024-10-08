import random
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB connection details
token = "your_token"
org = "your_org"
bucket = "your_bucket"
url = "your_url"

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Function to generate a random data point between 5 and 50
def generate_data_point():
    return random.uniform(5, 50)

# Tag and field structure
tags = {
    "location": "sensor_1",
    "device": "device_A"
}

# Generate 5000 data points in one batch
data_points = []
start_time = time.time()

for i in range(5000):
    fields = {
        "value": generate_data_point()
    }
    point = Point("measurement_name") \
        .tag("location", tags["location"]) \
        .tag("device", tags["device"]) \
        .field("value", fields["value"]) \
        .time(int(time.time_ns()), WritePrecision.NS)

    data_points.append(point)
    time.sleep(0.005)  # Wait for 0.005 seconds

# Send all data points in one batch
write_api.write(bucket=bucket, org=org, record=data_points)

# Closing client
client.close()

end_time = time.time()
print(f"Completed sending 5000 data points in {end_time - start_time} seconds.")
