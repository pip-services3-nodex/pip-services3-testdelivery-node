#!/usr/bin/env python3

import os
import json
import shutil

# Check for component file
path = os.path.abspath(os.path.dirname(__file__))
with open(f"{path}/component.json", "r", encoding="utf-8") as f:
    component = json.load(f)
container = component["name"]

# Set image name
build_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}-build"

# Remove build files
if os.path.exists(f"{path}/obj"):
    shutil.rmtree(f"{path}/obj")

# Copy private keys to access git repo
print("GIT_PRIVATE_KEY" in os.environ)
print(os.environ["GIT_PRIVATE_KEY"] != "")
print(os.environ["GIT_PRIVATE_KEY"] == None)
print(not os.environ["GIT_PRIVATE_KEY"])

if not os.path.exists(f"{path}/docker/id_rsa"):
    if "GIT_PRIVATE_KEY" in os.environ and os.environ["GIT_PRIVATE_KEY"] != "":
        print("Creating docker/id_rsa from environment variable...")
        with open(f"{path}/docker/id_rsa", "w") as f:
            f.write(os.environ["GIT_PRIVATE_KEY"])
    elif os.path.exists("~/.ssh/id_rsa"):
        print("Copying ~/.ssh/id_rsa to docker...")
        shutil.copyfile("~/.ssh/id_rsa", "{path}/docker")
    else:
        print("Missing ~/.ssh/id_rsa file...")
        with open(f"{path}/docker/id_rsa", "w") as f:
            f.write("")

# Copy .npmrc to docker folder to use it inside container
if not os.path.exists(f"{path}/docker/.npmrc"):
    if "NPM_TOKEN" in os.environ and os.environ["NPM_TOKEN"] != "":
        print("Creating docker/.npmrc from environment variable...")
        with open(f"{path}/docker/.npmrc", "w") as f:
            token = os.environ["NPM_TOKEN"]
            f.write(f"//registry.npmjs.org/:_authToken={token}")
    elif os.path.exists("~/.npmrc"):
        print("Putting ~/.npmrc to docker folder...")
        shutil.copyfile(f"~/.npmrc", "{path}/docker")
    else:
        print("Missing ~/.npmrc file...")
        with open(f"{path}/docker/.npmrc", "w") as f:
            f.write("")

# Build docker image
os.system(f"docker build -f '{path}/docker/Dockerfile.build' -t {build_image} .")

# Create and copy compiled files, then destroy
os.system(f"docker create --name {container} {build_image}")
os.system(f"docker cp '{container}:/app/obj' '{path}/obj'")
os.system(f"docker rm {container}")

# Verify that obj folder created after build
if not os.path.exists(f"{path}/obj"):
    raise "obj folder doesn't exist in root dir. Build failed. Watch logs above."
