import requests
import json

# Define the API endpoint and the API key
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key_here"

# Define the location
location = "London,uk"

# Send a GET request to the API endpoint
response = requests.get(api_endpoint, params={"q": location, "appid": api_key})

# Parse the response JSON
weather_data = response.json()

# Extract and print the weather data
print("Weather in {}: {} and {}°C".format(location, weather_data["weather"][0]["description"], weather_data["main"]["temp"] - 273.15))