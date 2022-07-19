#!/usr/bin/env python3

import os
import json
import shutil

# Check for component file
path = os.path.abspath(os.path.dirname(__file__))
with open(f"{path}/component.json", "r", encoding="utf-8") as f:
    component = json.load(f)

# Set image name
build_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}-build"
test_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}-test"
rc_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}"
latest_image = f"{component['registry']}/{component['name']}:latest"

# Remove docker images
os.system(f"docker rmi {test_image} --force")
os.system(f"docker rmi {rc_image} --force")
os.system(f"docker rmi {latest_image} --force")

with os.popen("docker images -f dangling=true -q") as f:
    dangling_images = f.read()
for i in dangling_images.split("\n"):
    if i:
        os.system(f"docker rmi -f {i}")  # remove dangling images

os.system("docker image prune --force")

# Remove existed containers
with os.popen("docker ps --filter status=exited") as f:
    dangling_containers = f.read()
for c in dangling_containers.split("\n")[1:]:
    if c:
        os.system(f"docker rm {c.split(' ')[0]}")  # remove exited containers

# Remove unused volumes
with os.popen("docker volume ls -f dangling=true") as f:
    dangling_volumes = f.read()
for v in dangling_volumes.split("\n")[1:]:  # skip headings of docker volume ls result
    print(v)
    if v:
        os.system(f"docker volume rm -f {v.split(' ')[-1]}")  # remove dangling volumes

# Remove cash and temp files 
try:
    shutil.rmtree(f"{path}/obj")
    shutil.rmtree(f"{path}/node_modules")
except OSError:
    pass
