from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')

API_KEY = "0869a893baff5f431715c018db8f72a6"  # API Key for OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/"

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    """
    Fetch weather data based on city name or coordinates.

    Query Parameters:
    - city: Name of the city (optional)
    - lat: Latitude (optional)
    - lon: Longitude (optional)
    - unit: Temperature unit (default is metric)
    """
    city = request.args.get('city', '')
    unit = request.args.get('unit', 'metric')  # Default to Celsius
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')

    if city:
        weather_data = get_weather_data(city, unit)
        return jsonify(weather_data)
    elif lat and lon:
        weather_data = get_weather_data_by_coords(lat, lon, unit)
        return jsonify(weather_data)
    return jsonify({'error': 'City or Coordinates not provided'})

@app.route('/forecast', methods=['GET'])
def forecast():
    """
    Fetch weather forecast data based on coordinates.

    Query Parameters:
    - lat: Latitude
    - lon: Longitude
    - unit: Temperature unit (default is metric)
    """
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')
    unit = request.args.get('unit', 'metric')  # Accept unit parameter (default to metric)

    if lat and lon:
        forecast_data = get_forecast_data(lat, lon, unit)
        return jsonify(forecast_data)
    return jsonify({'error': 'Latitude and Longitude not provided'})

def get_weather_data(city, unit):
    """
    Retrieve weather data for a specified city.

    Parameters:
    - city: Name of the city
    - unit: Temperature unit

    Returns:
    - JSON response from OpenWeatherMap API
    """
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units={unit}"
    response = requests.get(url)
    return response.json()

def get_weather_data_by_coords(lat, lon, unit):
    """
    Retrieve weather data based on latitude and longitude.

    Parameters:
    - lat: Latitude
    - lon: Longitude
    - unit: Temperature unit

    Returns:
    - JSON response from OpenWeatherMap API
    """
    url = f"{BASE_URL}weather?lat={lat}&lon={lon}&appid={API_KEY}&units={unit}"
    response = requests.get(url)
    return response.json()

def get_forecast_data(lat, lon, unit):
    """
    Retrieve weather forecast data based on latitude and longitude.

    Parameters:
    - lat: Latitude
    - lon: Longitude
    - unit: Temperature unit

    Returns:
    - JSON response from OpenWeatherMap API
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units={unit}"  # Include unit in API call
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch forecast data'}

if __name__ == '__main__':
    app.run(debug=True)