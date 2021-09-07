from datetime import datetime
from types import TracebackType

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "eehoW7NSFeObcVPPN9evABWtlJG9jBjgLUs_arDuGOqJPGsYAHJ6hN2XTGakbhPhFsxecCPa-NhLytdgqvvU4w=="
org = "skymind"
bucket = "python-bucket"

client = InfluxDBClient(url="http://localhost:8086", token=token)

# Create a query and pass the query to the api
query = f'from(bucket: "{bucket}") |> range(start: -1h) \
        |> filter(fn:(r) => r._measurement == "memory")'

tables = client.query_api().query(query, org=org)

for i, table in enumerate(tables):
    print(f"Table {i}")
    for row in table:
        # print(record)
        print(row.get_field())
        print(row.get_value())
