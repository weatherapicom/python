[![Ceasefire Now](https://badge.techforpalestine.org/default)](https://techforpalestine.org/learn-more)

-----

# WeatherAPI.com Python Client

A comprehensive and robust Python client designed for seamless integration with the **WeatherAPI.com API**. This library empowers developers to effortlessly fetch a vast array of weather and geolocation data, simplifying the development of weather-aware applications.

-----

## Table of Contents

  * [Introduction](https://www.google.com/search?q=%23introduction)
  * [Key Features](https://www.google.com/search?q=%23key-features)
  * [Getting Started](https://www.google.com/search?q=%23getting-started)
      * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      * [API Key Acquisition](https://www.google.com/search?q=%23api-key-acquisition)
  * [Installation & Usage](https://www.google.com/search?q=%23installation--usage)
      * [Installation via pip](https://www.google.com/search?q=%23installation-via-pip)
      * [Installation via Setuptools](https://www.google.com/search?q=%23installation-via-setuptools)
      * [Basic Usage Example](https://www.google.com/search?q=%23basic-usage-example)
  * [Authentication](https://www.google.com/search?q=%23authentication)
  * [API Endpoints Documentation](https://www.google.com/search?q=%23api-endpoints-documentation)
  * [Data Models Documentation](https://www.google.com/search?q=%23data-models-documentation)
  * [Requirements](https://www.google.com/search?q=%23requirements)
  * [Contributing](https://www.google.com/search?q=%23contributing)
  * [License](https://www.google.com/search?q=%23license)
  * [Author](https://www.google.com/search?q=%23author)
  * [Contact](https://www.google.com/search?q=%23contact)

-----

## Introduction

Welcome to the official Python client for **WeatherAPI.com**\! In today's data-driven world, integrating real-time and historical weather information is crucial for a multitude of applications, from smart home systems and agricultural tools to logistics management and travel planning.

WeatherAPI.com offers a leading **JSON/XML RESTful API** that delivers comprehensive weather and geo-data. This Python client acts as a streamlined interface, enabling you to quickly and efficiently access this rich dataset. Our goal is to provide a developer-friendly experience, allowing you to focus on building innovative features rather than handling the complexities of API communication.

-----

## Key Features

The WeatherAPI.com Python client provides access to an extensive range of weather and location-based data points, ensuring you have all the necessary information for your application's needs. Here's a detailed look at what you can retrieve:

  * **Real-time Weather:** Obtain current weather conditions for over 3 million locations globally. This includes temperature, humidity, wind speed and direction, pressure, precipitation, and more, updated in real time.
  * **14-Day Weather Forecast:** Get detailed weather forecasts for up to 14 days, available at both **daily and hourly intervals**. This is ideal for planning and predictive analytics.
  * **Historical Weather Data:** Access a vast archive of historical weather data, stretching back to January 1st, 2015. This feature is invaluable for research, analysis, and verifying past conditions.
  * **Future Weather Forecasts:** Look ahead with forecasts extending up to **365 days into the future**, providing long-term planning capabilities for various industries.
  * **Marine Weather & Tide Data:** Specialized data for marine environments, including wave height, swell direction, and comprehensive tide information, crucial for maritime activities.
  * **Granular Intervals:** Beyond daily and hourly, **15-minute intervals** are available for Enterprise users, offering exceptionally precise data for high-fidelity applications.
  * **Astronomy Data:** Retrieve astronomical information such as sunrise and sunset times, moon phase, moonrise, and moonset for any given location and date.
  * **Time Zone Information:** Accurate and up-to-date time zone data, essential for applications serving a global user base or requiring precise time synchronization.
  * **Location Data:** Comprehensive geographic details for any queried location, including coordinates, country, region, and more.
  * **Sports Data:** Access weather data tailored for sports events, providing conditions relevant to outdoor activities and game planning.
  * **Search/Autocomplete API:** A powerful feature that allows users to search for locations or provides autocomplete suggestions as they type, enhancing user experience.
  * **Weather Alerts:** Receive timely notifications and alerts for severe weather conditions, enabling proactive responses and safety measures.
  * **Air Quality Data (AQI):** Detailed information on air quality index (AQI) and its contributing pollutants, vital for health and environmental applications.
  * **Bulk Requests:** Optimize your data fetching by making bulk requests, allowing you to retrieve data for multiple locations or time periods in a single API call, reducing overhead and improving efficiency.

-----

## Getting Started

To begin using the WeatherAPI.com Python client, you'll need to set up your environment and obtain an API key.

### Prerequisites

  * **Python:** This client supports **Python 2.7** and **Python 3.4+**. We recommend using Python 3.x for optimal compatibility and performance with modern development practices.
  * **Internet Connection:** Required to communicate with the WeatherAPI.com servers.

### API Key Acquisition

Access to WeatherAPI.com's data is secured via an API key. This key acts as your unique identifier and authenticator.

1.  **Sign Up:** If you don't already have an account, visit the [WeatherAPI.com signup page](https://www.weatherapi.com/signup.aspx) to create one.
2.  **Locate Your API Key:** Once registered, log in to [your account](https://www.weatherapi.com/login.aspx). Your API key will be prominently displayed on your account dashboard.
3.  **Explore:** We encourage you to try out the API using our interactive [API Explorer](https://www.weatherapi.com/api-explorer.aspx) to understand its capabilities before diving into code.

-----

## Installation & Usage

You can install the WeatherAPI.com Python client using `pip` or Setuptools.

### Installation via pip

For most users, `pip` is the recommended method for installation. If the package is hosted on GitHub, you can install it directly:

```bash
pip install git+https://github.com/weatherapicom/python.git#egg=weatherapipython
```

  * **Note:** Depending on your system configuration, you might need elevated permissions to install packages globally. If you encounter permission errors, try running the command with `sudo` (on Linux/macOS) or in an administrator-level command prompt (on Windows):
    ```bash
    sudo pip install git+https://github.com/weatherapicom/python.git#egg=weatherapipython
    ```
    Alternatively, you can install it for your user only, which doesn't require `sudo`:
    ```bash
    pip install --user git+https://github.com/weatherapicom/python.git#egg=weatherapipython
    ```

Once installed, you can import the package into your Python scripts:

```python
import weatherapi
```

### Installation via Setuptools

If you prefer to install via [Setuptools](http://pypi.python.org/pypi/setuptools), navigate to the root directory of the cloned repository and run:

```bash
python setup.py install --user
```

  * To install the package for all users, use:
    ```bash
    sudo python setup.py install
    ```

After installation, you can import the package:

```python
import weatherapi
```

### Basic Usage Example

After installing the library and obtaining your API key, you can start making requests. The following example demonstrates how to configure the client and fetch astronomy data.

```python
from __future__ import print_function
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
# Replace 'YOUR_API_KEY' with the actual API key from your WeatherAPI.com account.
configuration = weatherapi.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'

# If your API key requires a prefix (e.g., Bearer), uncomment and set it:
# configuration.api_key_prefix['key'] = 'Bearer'

# Create an instance of the API class
api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))

# Define request parameters
# 'q': The location query. Can be a US Zipcode, UK Postcode, Canada Postalcode,
#      IP address, Latitude/Longitude (decimal degree), or city name.
#      Refer to the WeatherAPI.com documentation for more details on request parameters:
#      https://www.weatherapi.com/docs/#intro-request
q = 'London' # Example: City name
dt = '2025-06-30' # Example: Date in YYYY-MM-DD format (on or after 1st Jan, 2015)

try:
    # Call the Astronomy API endpoint
    print(f"Fetching astronomy data for '{q}' on '{dt}'...")
    api_response = api_instance.astronomy(q, dt)
    pprint(api_response)
    print("Astronomy data fetched successfully!")

except ApiException as e:
    # Handle API-specific exceptions, such as invalid API key, rate limits, etc.
    print(f"Error when calling APIsApi->astronomy: {e}\n")
except Exception as e:
    # Handle other general exceptions
    print(f"An unexpected error occurred: {e}\n")

```

-----

## Authentication

Authentication to the WeatherAPI.com API is straightforward and relies on your unique API key. This key must be passed as a query parameter in every API request.

  * **API Key Parameter Name:** `key`
  * **Location:** URL query string

**Example:**
`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London`

**Security Notice:** If you suspect your API key has been compromised, you can easily regenerate a new one from your [WeatherAPI.com account dashboard](https://www.weatherapi.com/login.aspx) by clicking the "Regenerate" button next to your API key.

-----

## API Endpoints Documentation

The `weatherapi` client provides direct access to all WeatherAPI.com endpoints. Below is a summary of the available methods and their corresponding HTTP requests. For detailed information on request parameters and response structures for each endpoint, please refer to the auto-generated documentation files in the `docs/` directory of this repository (e.g., `docs/APIsApi.md`).

| Class     | Method                                 | HTTP Request              | Description                       |
| :-------- | :------------------------------------- | :------------------------ | :-------------------------------- |
| `APIsApi` | [`astronomy`](https://www.google.com/search?q=docs/APIsApi.md%23astronomy)           | `GET /astronomy.json`     | Astronomy API                     |
| `APIsApi` | [`forecast_weather`](https://www.google.com/search?q=docs/APIsApi.md%23forecast_weather) | `GET /forecast.json`      | Forecast API                      |
| `APIsApi` | [`future_weather`](https://www.google.com/search?q=docs/APIsApi.md%23future_weather) | `GET /future.json`        | Future API                        |
| `APIsApi` | [`history_weather`](https://www.google.com/search?q=docs/APIsApi.md%23history_weather) | `GET /history.json`       | History API                       |
| `APIsApi` | [`ip_lookup`](https://www.google.com/search?q=docs/APIsApi.md%23ip_lookup)           | `GET /ip.json`            | IP Lookup API                     |
| `APIsApi` | [`marine_weather`](https://www.google.com/search?q=docs/APIsApi.md%23marine_weather) | `GET /marine.json`        | Marine Weather API                |
| `APIsApi` | [`realtime_weather`](https://www.google.com/search?q=docs/APIsApi.md%23realtime_weather) | `GET /current.json`       | Realtime API                      |
| `APIsApi` | [`search_autocomplete_weather`](https://www.google.com/search?q=docs/APIsApi.md%23search_autocomplete_weather) | `GET /search.json`        | Search/Autocomplete API           |
| `APIsApi` | [`time_zone`](https://www.google.com/search?q=docs/APIsApi.md%23time_zone)           | `GET /timezone.json`      | Time Zone API                     |

All URIs are relative to the base URL: `https://api.weatherapi.com/v1`.

-----

## Data Models Documentation

The `weatherapi` client also includes Python representations of the data structures (models) returned by the API. These models help you work with the API responses in a structured and type-safe manner. For a detailed description of each model and its properties, please refer to the respective documentation files in the `docs/` directory (e.g., `docs/Current.md`).

  * [`Alerts`](https://www.google.com/search?q=docs/Alerts.md)
  * [`AlertsAlert`](https://www.google.com/search?q=docs/AlertsAlert.md)
  * [`ArrayOfSearch`](https://www.google.com/search?q=docs/ArrayOfSearch.md)
  * [`Astronomy`](https://www.google.com/search?q=docs/Astronomy.md)
  * [`AstronomyAstro`](https://www.google.com/search?q=docs/AstronomyAstro.md)
  * [`Current`](https://www.google.com/search?q=docs/Current.md)
  * [`CurrentAirQuality`](https://www.google.com/search?q=docs/CurrentAirQuality.md)
  * [`CurrentCondition`](https://www.google.com/search?q=docs/CurrentCondition.md)
  * [`Error400`](https://www.google.com/search?q=docs/Error400.md)
  * [`Error401`](https://www.google.com/search?q=docs/Error401.md)
  * [`Error403`](https://www.google.com/search?q=docs/Error403.md)
  * [`Forecast`](https://www.google.com/search?q=docs/Forecast.md)
  * [`ForecastAstro`](https://www.google.com/search?q=docs/ForecastAstro.md)
  * [`ForecastCondition`](https://www.google.com/search?q=docs/ForecastCondition.md)
  * [`ForecastDay`](https://www.google.com/search?q=docs/ForecastDay.md)
  * [`ForecastDayCondition`](https://www.google.com/search?q=docs/ForecastDayCondition.md)
  * [`ForecastForecastday`](https://www.google.com/search?q=docs/ForecastForecastday.md)
  * [`ForecastHour`](https://www.google.com/search?q=docs/ForecastHour.md)
  * [`Ip`](https://www.google.com/search?q=docs/Ip.md)
  * [`Location`](https://www.google.com/search?q=docs/Location.md)
  * [`Marine`](https://www.google.com/search?q=docs/Marine.md)
  * [`MarineForecastday`](https://www.google.com/search?q=docs/MarineForecastday.md)
  * [`MarineHour`](https://www.google.com/search?q=docs/MarineHour.md)
  * [`Search`](https://www.google.com/search?q=docs/Search.md)

-----

## Requirements

The `weatherapipython` client has the following Python version requirements:

  * **Python 2.7**
  * **Python 3.4+**

-----

## Contributing

We welcome and appreciate contributions from the community\! If you have suggestions for new features, improvements, or bug fixes, please feel free to:

1.  **Open an Issue:** Describe the bug or suggest an enhancement on the [Issues page](https://www.google.com/search?q=https://github.com/weatherapicom/python/issues).
2.  **Submit a Pull Request:** If you've implemented a fix or a new feature, fork the repository, make your changes, and submit a pull request. We'll review it as soon as possible.

We are committed to making this client as useful and robust as possible, and your input is invaluable\!

-----

## License

This project is open-source and distributed under the **MIT License**. For the full details, please refer to the `LICENSE` file within this repository.

-----

## Author

This Python client is provided by **WeatherAPI.com**.

-----

## Contact

If you have any questions, require further assistance, or have suggestions, please don't hesitate to [contact us directly](https://www.weatherapi.com/contact.aspx).

-----
