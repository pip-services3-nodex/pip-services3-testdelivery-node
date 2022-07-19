#!/usr/bin/env python3

import os
import time
import requests
import json

# Check for component file
path = os.path.abspath(os.path.dirname(__file__))
with open(f"{path}/component.json", "r", encoding="utf-8") as f:
    component = json.load(f)

# Set image name
rc_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}"
latest_image = f"{component['registry']}/{component['name']}:latest"
os.environ["IMAGE"] = rc_image

# Build docker image
os.system(f"docker build -f {path}/docker/Dockerfile -t {rc_image} -t {latest_image} .")
print(f"\nBuilded run images:\n{rc_image}\n{latest_image}\n")

# Set docker machine ip (on windows not localhost)
if "DOCKER_IP" in os.environ:
    docker_ip = os.environ["DOCKER_IP"]
else:
    docker_ip = "localhost"

# Set http port if default value overwritten
if "HTTP_PORT" in os.environ:
    http_port = os.environ["HTTP_PORT"]
else:
    http_port = "8080"

# Set http route to test container
if "HTTP_ROUTE" in os.environ:
    http_route = os.environ["HTTP_ROUTE"]
else:
    http_route = "/heartbeat"

# Test runtime container
try:
    os.system(f"docker-compose -f {path}/docker/docker-compose.yml down")
    os.system(f"docker-compose -f {path}/docker/docker-compose.yml up -d")

    # Test using curl
    time.sleep(10)
    r = requests.get(f"http://{docker_ip}:{http_port}{http_route}")
    if (r.status_code == 0):
        print("The runtime container was successfully built and tested.")
except:
    # Output container logs if web request failed
    containers_statuses = os.popen(f"docker-compose -f {path}/docker/docker-compose.yml ps").read()
    # Parse docker-compose list of containers
    for container_status in containers_statuses.split("\n")[2:]:
        container_name = container_status.split(" ")[0]
        print(f"\nLogs of '{container_name}' container:")
        os.system(f"docker logs {container_name}")
    raise Exception("Error on testing run container. Watch logs above")
finally:
    os.system(f"docker-compose -f {path}/docker/docker-compose.yml down")
