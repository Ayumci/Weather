# Imports
import requests


# Api
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key_here"


while True:

#   Asks user for location
    location = input("\nPlease enter the location or 'quit' to exit: ")

    if location.lower() == "quit":
        break

    print(f"\nFetching weather data for {location}...")

#   Fetches weather data from api
    response = requests.get(api_endpoint, params={"q": location, "appid": api_key})
    
#   Checks if the response is valid    
    if response.status_code == 200:

#       Converts the response to json   
        weather_data = response.json()
        
#       Extract and print the weather data
        print("Weather in {}: {} and {:.2f}°C".format(
            location, 
            weather_data["weather"][0]["description"], 
            weather_data["main"]["temp"] - 273.15
        ))
        print("Humidity: {}%".format(weather_data["main"]["humidity"]))
        print("Wind Speed: {} m/s".format(weather_data["wind"]["speed"]))
    else:
        print("Failed to fetch weather data. Please check your location and try again.")
