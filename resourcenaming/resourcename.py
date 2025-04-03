# Simple naming tool for Cloud Resources

import os
import json

COUNTERS_FILE = "resource_counters.json"
RESOURCES_FILE = "resource_list.txt"


def get_counters():
    # Gets the counters dict
    if os.path.exists(COUNTERS_FILE):
        with open(COUNTERS_FILE, "r") as f:
            try:
                counters = json.load(f)
            except json.JSONDecodeError:
                counters = {}
    else:
        counters = {}
    return counters


def save_counters(counters):
    # Saves the counters dict to file
    with open(COUNTERS_FILE, "w") as f:
        json.dump(counters, f)


def generate_resource_name(deployed_year, proj_name, deployed_type, deployed_ver, deployed_env):
    # Generates a resource name with a sequential 5-digit number and writes to file if unique.

    base_name = f"{deployed_year}-{proj_name}-{deployed_type}-{deployed_ver}-{deployed_env}"
    counters = get_counters()

    counter = counters.get(base_name, 0)

    if counter > 99999:
        raise ValueError("Too many resources generated.")

    unique_id = str(counter).zfill(5)
    res_name = f"{base_name}-{unique_id}"
    counters[base_name] = counter + 1
    save_counters(counters)

    if not resource_exists(res_name, RESOURCES_FILE):
        with open(RESOURCES_FILE, "a") as f:
            f.write(res_name + "\n")

    return res_name


def resource_exists(res_name, resources_file):
    # Checks if a resource name already exists in the given file.
    if os.path.exists(resources_file):
        with open(resources_file, "r") as f:
            for line in f:
                if line.strip() == res_name:
                    return True
    return False


# Get user input
deployed_year = input("Year? ")
proj_name = input("Projectname? ").lower()
deployed_type = input("Type? ").lower()
deployed_ver = input("Version? ")
deployed_env = input("Environment? prod, dev, or test: ").lower()

# Generate and print the resource name
resource_name = generate_resource_name(
    deployed_year, proj_name, deployed_type, deployed_ver, deployed_env)
print(resource_name)
