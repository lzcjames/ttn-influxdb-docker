import time
import ttn
from dbclient import InfluxDB

app_id = "YOUR TTN APP ID"
accesskey = "YOUR TTN ACCESS KEY" 

def uplink_callback(msg, client):
  device = msg.dev_id
  temperature = msg.payload_fields.temperature
  influxdb.write_data(device, temperature)


influxdb = InfluxDB() 
handler = ttn.HandlerClient(app_id, access_key) 
mqtt_client = handler.data() 
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()
