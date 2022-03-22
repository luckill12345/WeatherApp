import requests
import json


def parsedata():
    file = open("location.txt", "r+")
    x = file.read()
    print("Read String is : ", x)
    file.close()
    y = json.loads(x)
    latitude = str(y["latitude"])
    longitude = str(y["longitude"])
    callapi("https://api.openweathermap.org/data/2.5/onecall?lat=" + latitude + "&lon=" + longitude + "&exclude=minutely&appid=")


def callapi(url):
    api_key = "94236d90083a95c4fec7c9f9f03c9d88"
    api_url = url + api_key
    print(api_url)
    response = requests.get(api_url)
    print(response.status_code)
    return response.json()


parsedata()


