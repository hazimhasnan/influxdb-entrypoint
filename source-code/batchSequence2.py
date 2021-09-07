from datetime import datetime
import random

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "eehoW7NSFeObcVPPN9evABWtlJG9jBjgLUs_arDuGOqJPGsYAHJ6hN2XTGakbhPhFsxecCPa-NhLytdgqvvU4w=="
org = "skymind"
bucket = "python-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

sequence = []
percent = 20
for i in range(20):
  percent+=i
  sequence.append(f"water-level,tank=tank1 used_percent={percent}")

for i in range(20):
  percent = random.randrange(20, 40)
  sequence.append(f"water-level,tank=tank2 used_percent={percent}")

for i in sequence:
  print(i)

write_api.write(bucket, org, sequence)