import requests
from requests.auth import HTTPBasicAuth

def make_rest_call(username, password):
    url = "http://localh2-env.eba-rpvpzjqz.eu-central-1.elasticbeanstalk.com/plug/48551917CE6C"

    # ophalen en verwerken van de username en password
    auth = HTTPBasicAuth(username, password)

    try:
        #call maken
        response = requests.get(url, auth=auth)

        # als er een connectie is print de response uit anders error printen
        if response.status_code == 200:
            print("REST call successful.")
            print("Response:")
            print(response.text)
        else:
            print(f"Failed to make the REST call. Status Code: {response.status_code}")
            print("Response:")
            print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # username en password via input zoat niemand erbij kan
    username = input("Enter username: ")
    password = input("Enter password: ")

    make_rest_call(username, password)
