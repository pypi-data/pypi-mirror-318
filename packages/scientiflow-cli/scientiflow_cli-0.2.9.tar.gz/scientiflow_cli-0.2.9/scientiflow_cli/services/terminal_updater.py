from scientiflow_cli.services.request_handler import make_auth_request
def init_output():
    try:
        with open("output.txt", 'w') as f:
            f.write('')
    except:
        pass

def capture_output(text: str):
    try:
        with open("output.txt", 'a') as f:
            f.write(text+"\n")
        print(text+"\n")
    except:
        pass

def update_terminal_output(project_job_id: int):
    try:
        with open("output.txt", 'r') as f:
            terminal_output = f.read()
    except:
        pass
    body = {"project_job_id": project_job_id, "terminal_output": terminal_output}
    make_auth_request(endpoint="/agent-application/update-terminal-output", method="POST", data=body, error_message="Unable to update terminal output!")
    print("[+] Terminal output updated successfully.")
