import socket
import requests
import time

def register_demo(debug=False):
    for attempt in range(10):
        try:
            local_ip = socket.gethostbyname(socket.gethostname())
            response = requests.post(
                "http://hocmay-svc/aiplatform-api/demo/register/", 
                json={"demo_ip": local_ip}, 
                headers={"Content-Type": "application/json"}
            )
            if response.ok:
                if debug:
                    print("IP registered successfully.")
                return True
            else:
                if debug:
                    print(f"Attempt {attempt + 1}: Failed: {response.text}")
        except (socket.error, requests.exceptions.RequestException) as e:
            if debug:  # Print errors only if debug is True
                print(f"Attempt {attempt + 1}: Error: {e}")
        
        time.sleep(2)  # Wait for 2 seconds before retrying

    if debug:
        print("Failed to register IP after 10 attempts.")
    return False
