# AI-Powered Weather Outfit Recommendation System

This project retrieves weather forecast data using the OpenWeather API and generates AI-powered outfit recommendations using the Gemini API.

The program converts a city name into geographic coordinates, retrieves weather information, and then uses a large language model to suggest appropriate clothing based on the weather conditions.

---

## Features

- Convert city names into geographic coordinates using the OpenWeather Geocoding API  
- Retrieve short-term weather forecast data  
- Extract key weather metrics such as temperature, humidity, and wind speed  
- Generate AI-powered outfit recommendations using the Gemini API  

---

## Technologies Used

- Python  
- OpenWeather API  
- Gemini API  
- Requests  
- Environment variables (`.env`)  

---

## Setup

To run this project, you need API keys from both **Gemini** and **OpenWeather**.

### 1. Obtain API keys from

- https://openweathermap.org/api  
- https://ai.google.dev/gemini-api/docs/api-key  

### 2. Create a `.env` file in the same directory as the program

### 3. Add your API keys to the `.env` file in the following format

```
OPENWEATHER_API_KEY=your_openweather_key
GEMINI_API_KEY=your_gemini_key
```

---

## Example Output

```
Weather forecast for the next three hours
The weather in Tokyo, JP is light rain.
Temperature: 21°C (feels like 20°C)
Humidity: 78%
Wind speed: 3.2 m/s
Outfit suggestion: Light jacket recommended due to cool temperature and rain.
```
