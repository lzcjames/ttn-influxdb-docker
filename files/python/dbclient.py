from influxdb_client import InfluxDBClient,Point
from influxdb_client.client.write_api import SYNCHRONOUS

mytoken = "aaabbbccc"
bucketName = "lora-projet"
myurl = "http://localhost:9999"
org = "univ"
class InfluxDB:
    def __init__(self):
        self.client = InfluxDBClient(url=myurl, token=mytoken)

    def write_data(self, device, temperature):
        point = Point(device)\
            .tag("location", "France")\
            .field("temperature", temperature)
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucketName, org, point)
        print("---------------------------------------------")
        print("Device:", device, "temperature:", temperature)
        print("INFO: data has been written")