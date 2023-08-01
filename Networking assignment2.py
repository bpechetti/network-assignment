import requests
import time
from tabulate import tabulate

# List of subdomains to check
subdomains = ["vlearnv.herovired.com", "herovired.com", "subdomain3.example.com"]

def check_subdomain_status(subdomain):
    try:
        response = requests.get(f"http://{subdomain}")
        return "UP" if response.status_code == 200 else "DOWN"
    except requests.RequestException:
        return "DOWN"

def update_status_table():
    status_data = []

    for subdomain in subdomains:
        status = check_subdomain_status(subdomain)
        status_data.append([subdomain, status])

    return status_data

def print_status_table(status_data):
    headers = ["Subdomain", "Status"]
    print(tabulate(status_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    while True:
        status_data = update_status_table()
        print_status_table(status_data)
        time.sleep(5)  # Wait for 1 minute
