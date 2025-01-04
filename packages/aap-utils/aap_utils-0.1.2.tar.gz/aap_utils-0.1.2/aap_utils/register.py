import socket
import requests
import time
import os

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
                url, namespace = create_url()
                # print(f"The demo service is at {namespace}.your_custorm_domain/demo/. Eg: {url}")
                print(f"The demo service is at {url}")
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



def create_url(domain_name = "aiplatform.vcntt.tech"):
    # Define the static domain name    
    
    # Read the KERNEL_NAMESPACE environment variable
    kernel_namespace = os.getenv("KERNEL_NAMESPACE")
    
    # Validate the environment variable
    if not kernel_namespace:
        kernel_namespace="undefined"
    
    # Replace 'machinelearning' with 'appmachinepublic' in KERNEL_NAMESPACE
    if kernel_namespace.startswith("machinelearning"):
        transformed_namespace = kernel_namespace.replace("machinelearning", "appmachinepublic", 1)
    else:
        raise ValueError(f"The KERNEL_NAMESPACE '{kernel_namespace}' does not follow the expected format.")
    
    # Create the final URL
    url = f"https://{transformed_namespace}.{domain_name}/demo/"
    return url, transformed_namespace
