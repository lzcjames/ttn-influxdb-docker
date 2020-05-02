import requests
import json
from dbclient import InfluxDB

# For more info about @url, see: https://www.thethingsnetwork.org/docs/applications/storage/api.html and
# https://www.youtube.com/watch?v=kVf8GmCbOuE&index=3&list=PLM8eOeiKY7JVwrBYRHxsf9p0VM_dVapXl
url = 'https://example.data.thethingsnetwork.org/api/v2/query/arduino0' 

accesskey = "YOUR TTN ACCESS KEY" 
headers = {'Accept': 'application/json', 'Authorization': 'key '+ accesskey}

result = requests.get(url,headers=headers)
print(result)
dataObjs = result.json()
influxdb = InfluxDB() 

for data in dataObjs:
    device = data["device_id"]
    temperature = data["temperature"]
    influxdb.write_data(device, temperature)
