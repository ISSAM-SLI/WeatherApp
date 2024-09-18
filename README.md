# Weather App

## Description

This is a simple weather web application built using Flask. It provides current weather information and a 5-day weather forecast based on the city or your current location. The app is styled with custom CSS and uses the OpenWeatherMap API to fetch weather data.

## Project Structure

- `static/`: Contains CSS and image files.
  - `styles.css`: The main stylesheet for the application.
  - `images/last.png`: Background image for the app.
- `templates/`: Contains HTML template files.
  - `index.html`: The main HTML file rendered by Flask.
- `weather.py`: The main Python file for the Flask application.
- `vercel.json`: Configuration file for deploying the app on Vercel.
- `requirements.txt`: Lists the Python dependencies for the project.

## Live Demo

You can view the live version of the app [here](https://weatherapp-pi-one.vercel.app/).

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
2. Navigate to the project directory:
   cd <project-directory>
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the application:
   python3 weather.py

Deployment
The application is deployed on Vercel. The vercel.json file is configured to handle the deployment settings. 
Notes
Resizing for Fit: If the application appears too large or does not fit your screen properly, you can adjust the zoom level of your browser.
