from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "Rvkv9YM6U4S9rcY-8gijLBRAQfILr2ixkH1JXE-ozM2uw-A5Nk9wI3VHcupXNAJ-9wd4qa9guCKUN59athWp5w=="
org = "skymind"
bucket = "python-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Creating point object
point = Point("mem")\
  .tag("host", "host1")\
  .field("used_percent", 25.43234543)\
  .time(datetime.utcnow(), WritePrecision.NS)

# Write to the bucket
write_api.write(bucket, org, point)