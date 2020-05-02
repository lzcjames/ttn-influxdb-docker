# ttn-influxdb-docker

A simple app under Docker-compose which lets The Things Network data transfer into InfluxDB using MQTT protocol or TTN Storage (REST) API

## Prerequisite

Docker Compose: 3.7

InfluxDB Image: 2.0.0-beta

Python Image: 3.7

## Project structure
```bash
ttn-influxdb-docker/
 |-- .env
 |-- docker-compose.yml
 |-- files
       |-- Dockerfile
       |-- python
              |-- httpclient.py
              |-- mqttclient.py
              |-- dbclient.py
              |-- requirements.txt
```

The `.env` file declares the values of the variables that are defined in docker-compose.yml, in this case it declares a InfluxDB user and password etc.

The `docker-compose.yml` file is used to describe and manage multiple containers as a set of interconnected services.

The `Dockerfile` file allows us to build a Docker image adapted to our needs, step by step.

The `requirements.txt` file will store a list of all Python packages and their version installed on the system in the current folder.

## Launch the app
In the console of the host machine (Windows in my case), type:

```
cd ttn-influxdb-docker
docker compose up
```

To navigate InfluxDB console, type 127.0.0.1:9999

Username: lorauser

Password: password
