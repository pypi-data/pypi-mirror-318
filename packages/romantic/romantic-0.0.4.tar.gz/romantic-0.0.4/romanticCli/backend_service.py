import requests

from romanticCli.auth import get_username, get_password

baseUrl = "https://romantic.up.railway.app"


def get_romantic_message(today=False):
    # Fetch username and password
    username = get_username()
    password = get_password()

    if today:
        url = f"{baseUrl}/api/lines?state=today"
    else:
        url = f"{baseUrl}/api/lines"

    # Send GET request to the backend with authentication
    response = requests.get(url, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Extract the 'data' field which contains the message
        romantic_message = response_data.get("data", "No message found")

        # Return the message
        return romantic_message
    else:
        # Handle error if the response is not successful
        return f"Error: {response.status_code} - {response.text}"



def send_secret_note(note):
    # Fetch username and password
    username = get_username()
    password = get_password()

    # Send POST request to the backend with authentication
    response = requests.post(f"{baseUrl}/api/secret_message", data=note, auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Extract the 'data' field which contains the message
        romantic_message = response_data.get("data", "No message found")

        # Return the message
        return romantic_message