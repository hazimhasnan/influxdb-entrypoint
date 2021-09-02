from influxdb_client import InfluxDBClient

client = InfluxDBClient(url="http://localhost:8086", token="Rvkv9YM6U4S9rcY-8gijLBRAQfILr2ixkH1JXE-ozM2uw-A5Nk9wI3VHcupXNAJ-9wd4qa9guCKUN59athWp5w==")

delete_api = client.delete_api()

# Delete Data
start = "1970-01-01T00:00:00Z"
stop = "2022-02-01T00:00:00Z"
delete_api.delete(start, stop, '_measurement="mem"', bucket='python-bucket', org='skymind')

# Close client
client.close()
