#!/usr/bin/env python3

import sys
import os
import json

# Check for component file
path = os.path.abspath(os.path.dirname(__file__))
with open(f"{path}/component.json", "r", encoding="utf-8") as f:
    component = json.load(f)

# Set image name
test_image = f"{component['registry']}/{component['name']}:{component['version']}-{component['build']}-test"
os.environ["IMAGE"] = test_image

# Run tests in docker container
try:
    os.system(f"docker-compose -f \"{path}/docker/docker-compose.test.yml\" down")
    exit_code = os.system(f"docker-compose -f \"{path}/docker/docker-compose.test.yml\" up --build --abort-on-container-exit --exit-code-from test")
finally:
    os.system(f"docker-compose -f \"{path}/docker/docker-compose.test.yml\" down")

# End script with exit code from tests
print(f"component test script exited with {exit_code}")
sys.exit(exit_code)
