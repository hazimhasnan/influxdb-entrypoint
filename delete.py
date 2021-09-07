from influxdb_client import InfluxDBClient

token = "eehoW7NSFeObcVPPN9evABWtlJG9jBjgLUs_arDuGOqJPGsYAHJ6hN2XTGakbhPhFsxecCPa-NhLytdgqvvU4w=="
bucket = "python-bucket"
org = "skymind"

client = InfluxDBClient(url ="http://localhost:8086", token=token)
delete_api = client.delete_api()

# Delete Data
start = "1970-01-01T00:00:00Z"
stop = "2022-02-01T00:00:00Z"
delete_api.delete(start, stop, '_measurement="memory"', bucket, org)

# Close client
client.close()
