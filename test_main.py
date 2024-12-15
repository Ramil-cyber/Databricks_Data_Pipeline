"""
Test Databricks Functionality
"""

import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SERVER_HOSTNAME = os.getenv("SERVER_HOSTNAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CLUSTER_ID = "1121-024828-5se7kk8r"
BASE_URL = f"https://{SERVER_HOSTNAME}/api/2.1"

# Validate environment variables
if not SERVER_HOSTNAME or not ACCESS_TOKEN:
    raise ValueError("SERVER_HOSTNAME and ACCESS_TOKEN must be set in the .env file.")


def check_cluster_existence(cluster_id: str, headers: dict) -> bool:

    try:
        response = requests.get(
            f"{BASE_URL}/clusters/get",
            headers=headers,
            params={"cluster_id": cluster_id},
        )
        response.raise_for_status()
        # Check if the response contains a valid file path
        # return response.json()
        return "cluster_id" in response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return False


def test_databricks():
    """
    Test if the Databricks file store path exists and is accessible.
    """
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    path_exists = check_cluster_existence(CLUSTER_ID, headers)
    assert path_exists, f"Cluster Id- {CLUSTER_ID} not found"
    print(f"Test successful: Cluster Id -  '{CLUSTER_ID}' exists and is accessible.")


if __name__ == "__main__":
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    print(check_cluster_existence(CLUSTER_ID, headers))
