import requests
import argparse
from simple_chalk import chalk
import time

API_KEY = '30a03f3a722f201f10f2fb50770646ae'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

while True:

    parser = argparse.ArgumentParser(description="Check the weather for a Location.")
    parser.add_argument("Location")
    args = parser.parse_args()

    url = f"{BASE_URL}?q={args.Location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print(chalk.red("Error: Unable to retrieve weather information."))
        exit()
    data = response.json()
    city = data["name"]
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    print("\nCurrent weather in ",city ,": \n\n")
    print( description )
    print("Temperature: ",temperature,"°C")
    print("Feels like: ",feels_like,"°C")
    print("Humidity: ",humidity,"%\n")
    time.sleep(3)

    