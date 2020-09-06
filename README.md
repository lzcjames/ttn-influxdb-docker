# ttn-influxdb-docker

A simple app under Docker-compose which lets The Things Network data transfer into InfluxDB using MQTT protocol or TTN Storage (REST) API.

> To use TTN Storage (REST) API, make sure you've already added Data Storage Interation in your TTN project, https://www.thethingsnetwork.org/docs/applications/integrations.html#add-an-integration

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

To navigate the InfluxDB console, type 127.0.0.1:9999

- Username: lorauser

- Password: password


### Good to know
Dockerfile can be also built, and run directly.
Example:
```bash
FROM debian:buster-slim
RUN apt-get update -y \
          && apt-get -y install openssh-server net-tools iputils-ping nano
		  
ENTRYPOINT tail -F /dev/null	
```

#### To build Dockerfile
`docker build -t TAGNAME_CONTAINER .`

#### To keep container running:

**solution 1**
The command `tail -F /dev/null` is always running in a container so that it keeps the container running.
Then, `docker run -dit TAGNAME_CONTAINER`

**solution 2**
Add `/bin/bash` in the end of command `docker run ...`
Then, `docker run -dit TAGNAME_CONTAINER /bin/bash`
An alternative command `docker run -dit --privileged=true TAGNAME_CONTAINER  "/sbin/init"` for using like `iptables`, `systemctl` in the container.

#### Limitations :(
The option `--network=host` lets a container to join the network of host, so it can ping the host. 
But if the host runs Docker Desktop for Window:
```
The Docker Desktop for Windows CAN NOT route traffic to a linux container but to a windows container.
```
Ref:https://docs.docker.com/docker-for-windows/networking/#i-cannot-ping-my-containers
