# AI-Powered Weather Outfit Recommendation System

This project is a Python-based application that retrieves short-term weather forecast data using the OpenWeather API and generates AI-powered outfit recommendations using the Gemini API.

It demonstrates how REST APIs and large language models can be combined to build a simple user-centered application. Instead of requiring users to manually enter geographic coordinates, the program allows them to input a city name, automatically converts it into latitude and longitude, retrieves forecast data, and generates practical clothing suggestions.

## Features

- Convert user-input city names into geographic coordinates using the OpenWeather Geocoding API
- Retrieve short-term weather forecast data using the OpenWeather Forecast API
- Extract key weather metrics such as temperature, feels-like temperature, humidity, weather description, and wind speed
- Generate AI-powered outfit recommendations using the Gemini API
- Configure LLM behavior with `system_instruction`, `temperature`, and `max_output_tokens`
- Organize logic into modular Python functions
- Handle API and data errors with exception handling
- Store API keys securely using environment variables in a `.env` file

## Workflow

User input (city name)  
→ Geocoding API converts city name to latitude and longitude  
→ Forecast API retrieves weather data  
→ Program parses JSON response and extracts key indicators  
→ Gemini API generates outfit recommendations based on weather conditions

## Technologies Used

- Python
- REST APIs
  - OpenWeather API (Geocoding and Forecast endpoints)
  - Gemini API
- requests
- python-dotenv
- JSON parsing
- environment variable management

## Project Structure

- `get_coordinates(city)`: Converts a city name into geographic coordinates
- `get_weather(lat, lon)`: Retrieves weather forecast data
- `generate_outfit_recommendation(...)`: Sends weather data to Gemini and generates clothing suggestions
- `main()`: Handles user input and program output

## Setup

To run this project, you need API keys from both OpenWeather and Gemini.

### 1. Get API keys
- OpenWeather API key from OpenWeather
- Gemini API key from Google AI Studio

### 2. Create a `.env` file
Create a `.env` file in the same directory as your Python script.

### 3. Add your API keys
```env
OPENWEATHER_API_KEY=your_openweather_key
GEMINI_API_KEY=your_gemini_key
```

---

## Example Program Output

```
📝 Weather forecast for the next three hours
☁️ Weather in Tokyo, JP: light rain
🌡️ Temperature: 21°C (feels like 20°C)
💧 Humidity: 78%
🌬️ Wind speed: 3.2 m/s
👔 Outfit suggestion:
Wear a light jacket and consider waterproof shoes or an umbrella because of the cool temperature and rain.
```
