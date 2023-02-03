import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/appsec/v1"
headers = {"User-Agent": "Python HMAC Example"}


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/applications", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        data_file = open("csvTest.csv", "w", newline='') #this can be any file type but I chose to write to a CSV file.
        for app in data["_embedded"]["applications"]:
            print(app["profile"]["name"]) # prints the app names to the console/terminal
            data_file.write(app["profile"]["name"]+'\n') # appends the app name to the file with a newline character
         
        data_file.close()
    else:
        print(response.status_code)
