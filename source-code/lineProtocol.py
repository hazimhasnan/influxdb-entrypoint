from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "eehoW7NSFeObcVPPN9evABWtlJG9jBjgLUs_arDuGOqJPGsYAHJ6hN2XTGakbhPhFsxecCPa-NhLytdgqvvU4w=="
org = "skymind"
bucket = "python-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

data = "memory,pc=pc1 used_percent=23.43234543"
write_api.write(bucket, org, data)
