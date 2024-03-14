import requests
import json

def get_weather( api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def show_weather(weather_data):
    if weather_data["cod"] != "404":
        city = weather_data["name"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        print(f"Weather in {city}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(" no city found!")

def main():
    api_key =  "0f3d4a757f1a3be06786e9ee282d6961"
    city = input("Enter any city: ")
    weather_data = get_weather(api_key, city)
    show_weather(weather_data)

if __name__ == "__main__":
    main()
