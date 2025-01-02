import requests
import os
import json

from scientiflow_cli.pipeline.get_jobs import get_jobs

def set_base_directory(auth_token: str) -> None:

    API_BASE: str = "https://www.backend.scientiflow.com/api"

    hostname = input("Enter the hostname for this: ")
    current_working_directory: str = os.getcwd()
    headers = { "Authorization": f"Bearer {auth_token}"}
    # sends a request to the create-server endpoint
    response = requests.post(f"{API_BASE}/servers/create-or-update-server", headers=headers, json={
      "hostname": hostname,
      "base_directory": current_working_directory,
      "description": ""
    })
    if response.status_code == 200:
        # stores the current working directory in a .config file
        config_path = os.path.expanduser("~/.scientiflow/config")
        current_working_directory = os.getcwd()
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as file:
            file.write(json.dumps({"BASE_DIR": current_working_directory}))
        print(f"Successfully set base directory!")
        return
    else:
        print("ERROR:", response.json()["flashNegativeMessage"])
        return