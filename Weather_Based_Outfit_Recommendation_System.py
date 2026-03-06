import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()  # call API_KEY
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)


# Define the function to obtain the city's corresponding latitude and longitude
def get_coordinates(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    # Prepare query parameters required by the API
    params = {
        "q": city,
        "limit": 1,
        "appid": openweather_api_key
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception if the HTTP status code is not in the 2xx range
        data = response.json()

        if not data:
            raise ValueError(f"City not found:{city}")  # Check if the result list is empty

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"The request to the geocoding API failed: {e}")  # Catch all network-related errors and HTTP errors caught by raise_for_status()
    except (KeyError, IndexError, TypeError) as e:
        raise ValueError(
            f"The API returns formatting anomalies or no coordinates found:{city}")  # Catch errors that happen when trying to access the data structure


# Define the funtion to derive weather data based on latitude and longitude
def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    # Prepare query parameters required by the API
    params = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "cnt": 1,
        "appid": openweather_api_key
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception if the HTTP status code is not in the 2xx range
        data = response.json()

        temp = data['list'][0]['main']['temp']
        feels_like = data['list'][0]["main"]["feels_like"]
        description = data['list'][0]["weather"][0]["description"]
        humidity = data['list'][0]['main']['humidity']
        wind_speed = data['list'][0]['wind']['speed']
        city = data['city']['name']
        country = data['city']['country']

        return temp, feels_like, description, humidity, wind_speed, city, country

    except requests.exceptions.RequestException as e:
        raise RuntimeError(
            f"The request to the weather API failed: {e}")  # Catch all network-related errors and HTTP errors caught by raise_for_status()
    except (KeyError, IndexError, TypeError) as e:
        raise ValueError(
            f"The weather API returns formatting anomalies or incomplete data for coordinates ({lat}, {lon})")  # Catch errors that happen when trying to access the data structure


# Define the funtion to get AI dressing suggestions with weather data
def generate_outfit_recommendation(temp, feels_like, description, humidity, wind_speed, city, country):
    prompt = f"""Based on the following weather data, recommend dressing suggestions in two sentences.
    temperature = {temp}
    feels like = {feels_like}
    weather description = {description}
    humidity = {humidity}
    wind_speed = {wind_speed}
    city = {city}
    country = {country}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return "Sorry, I couldn't generate a suggestion right now. Please wait a moment and try again later."


def main():
    print("Please enter city name: (e.g. 'New York' or 'Tokyo'), then press 'Enter'.")
    city_input = input("Enter city name: ").strip()
    if not city_input:
        print("City name cannot be empty.")
        return
    try:
        lat, lon = get_coordinates(city_input)

        temp, feels_like, description, humidity, wind_speed, city, country = get_weather(lat, lon)

        recommendation = generate_outfit_recommendation(
            temp, feels_like, description, humidity, wind_speed, city, country
        )

        print(f"""
📝 Weather forecast for the next three hours
☁️ Weather in {city}, {country}: {description}
🌡️ Temperature: {temp}°C (feels like {feels_like}°C)
💧 Humidity: {humidity}%
🌬️ Wind speed: {wind_speed} m/s
👔 Outfit suggestion:
{recommendation}
""")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")
        print(f"We recommend checking the temperature and dressing accordingly!")


if __name__ == "__main__":
    main()