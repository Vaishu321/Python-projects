# Let’s get real weather data using a free weather API:
import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

data.keys()
data.values()

# The API sends back data in JSON format (like a Python dictionary):
# The temperature is nested inside current, so to get it:

temperature = data['current']['temperature_2m']
print(f"Temperature in Paris: {temperature}°C")
# Output: Temperature in Paris: 20.0°C

# What is JSON? JSON (JavaScript Object Notation) is just a way to structure data, similar to CSV or Excel files. While CSV stores data in rows and columns, 
# JSON uses key-value pairs like Python dictionaries

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

# How it works
# You send a request to the API’s URL with parameters (like coordinates)
# The API processes your request and finds the data
# You receive JSON data back with the information
# You extract the specific parts you need
# The pattern is always the same: connect to an API, send requests, get data back, use it in your code. APIs are how modern software talks to each other.