import requests
import pwinput

from scientiflow_cli.cli.auth_utils import setAuthToken
import re

def login_user():
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email = input("Enter your email: ")
    if re.match(pattern, email):
       is_valid = True
    else:
       is_valid = False
    if is_valid:
      password = pwinput.pwinput("Enter your password: ")
      payload = {
        "email": email,
        "password": password,
        "device_name": "Google-Windows",
        "remember": True
      }
    else:
      print(f"'{email}' is not a valid email.")
      return
    # app_base_url = "https://www.backend.scientiflow.com"
    app_base_url = "https://www.backend.scientiflow.com/api"
    login_url = f"{app_base_url}/auth/login"
    response = requests.post(login_url, json=payload)
    if response.status_code == 200:
        print("Login successful!")
        auth_token = response.json().get("token")
        if auth_token:
            setAuthToken(auth_token)
        else:
            print("No token received from the server.")
    else:
        print("Login failed!")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")