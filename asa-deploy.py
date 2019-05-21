""" A simple script to take a base Cisco ASA 5506 Config and return a
    working config to be installed on a new 5506.
"""
import json

# open the configuration file
try:
    with open('asa-config.json', 'r') as file:
        configuration = json.loads(file.read())
except FileNotFoundError as e:
    print(f"Config file asa-config.json not found. {e}")

# open the base configuration for reading
try:
    with open('base-config.txt', 'r') as base_file:
        base_config = base_file.read()
        for key, value in configuration.items():
            base_config = base_config.replace(key.upper(), value)

except FileNotFoundError as e:
    print(f"Config file base-config.txt not found. {e}")

# open and write to the final config, output.txt
try:
    with open ('output.txt', 'w') as output:
        output.write(base_config)

except IOError as e:
    print(f"Error writing to output.txt. Check disk space {e}")


print("Cisco ASA Config created in output.txt")

