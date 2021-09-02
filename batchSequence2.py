from datetime import datetime
import random

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "Rvkv9YM6U4S9rcY-8gijLBRAQfILr2ixkH1JXE-ozM2uw-A5Nk9wI3VHcupXNAJ-9wd4qa9guCKUN59athWp5w=="
org = "skymind"
bucket = "python-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

sequence = []
percent = 20
for i in range(20):
  percent+=i
  sequence.append(f"mem,host=host1 used_percent={percent}")

for i in range(20):
  percent = random.randrange(20, 40)
  sequence.append(f"mem,host=host2 used_percent={percent}")

for i in sequence:
  print(i)

write_api.write(bucket, org, sequence)