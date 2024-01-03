[![Ceasefire Now](https://badge.techforpalestine.org/default)](https://techforpalestine.org/learn-more)

# Python client for WeatherAPI.com

# Introduction
WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy. 

We provide following data through our API:     
- Real-time weather
- 14 day weather forecast
- Historical Weather
- Marine Weather and Tide Data
- Future Weather (Upto 365 days ahead)
- Daily and hourly intervals
- 15 min interval (Enterprise only)
- Astronomy
- Time zone
- Location data
- Sports
- Search or Autocomplete API
- Weather Alerts
- Air Quality Data
- Bulk Request

# Getting Started    
You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!  

Try our weather API by using interactive [API Explorer](https://www.weatherapi.com/api-explorer.aspx).  

We also have SDK for popular framework/languages available on [Github](https://github.com/weatherapicom/) for quick integrations.  

If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).    

# Authentication    
API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.    

Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .      

##  key parameter  
key=YOUR API KEY

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/weatherapicom/python.git#egg=weatherapipython
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/weatherapicom/python.git#egg=weatherapipython`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.
dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format

try:
    # Astronomy API
    api_response = api_instance.astronomy(q, dt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->astronomy: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.weatherapi.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIsApi* | [**astronomy**](docs/APIsApi.md#astronomy) | **GET** /astronomy.json | Astronomy API
*APIsApi* | [**forecast_weather**](docs/APIsApi.md#forecast_weather) | **GET** /forecast.json | Forecast API
*APIsApi* | [**future_weather**](docs/APIsApi.md#future_weather) | **GET** /future.json | Future API
*APIsApi* | [**history_weather**](docs/APIsApi.md#history_weather) | **GET** /history.json | History API
*APIsApi* | [**ip_lookup**](docs/APIsApi.md#ip_lookup) | **GET** /ip.json | IP Lookup API
*APIsApi* | [**marine_weather**](docs/APIsApi.md#marine_weather) | **GET** /marine.json | Marine Weather API
*APIsApi* | [**realtime_weather**](docs/APIsApi.md#realtime_weather) | **GET** /current.json | Realtime API
*APIsApi* | [**search_autocomplete_weather**](docs/APIsApi.md#search_autocomplete_weather) | **GET** /search.json | Search/Autocomplete API
*APIsApi* | [**time_zone**](docs/APIsApi.md#time_zone) | **GET** /timezone.json | Time Zone API


## Documentation For Models

 - [Alerts](docs/Alerts.md)
 - [AlertsAlert](docs/AlertsAlert.md)
 - [ArrayOfSearch](docs/ArrayOfSearch.md)
 - [Astronomy](docs/Astronomy.md)
 - [AstronomyAstro](docs/AstronomyAstro.md)
 - [Current](docs/Current.md)
 - [CurrentAirQuality](docs/CurrentAirQuality.md)
 - [CurrentCondition](docs/CurrentCondition.md)
 - [Error400](docs/Error400.md)
 - [Error401](docs/Error401.md)
 - [Error403](docs/Error403.md)
 - [Forecast](docs/Forecast.md)
 - [ForecastAstro](docs/ForecastAstro.md)
 - [ForecastCondition](docs/ForecastCondition.md)
 - [ForecastDay](docs/ForecastDay.md)
 - [ForecastDayCondition](docs/ForecastDayCondition.md)
 - [ForecastForecastday](docs/ForecastForecastday.md)
 - [ForecastHour](docs/ForecastHour.md)
 - [Ip](docs/Ip.md)
 - [Location](docs/Location.md)
 - [Marine](docs/Marine.md)
 - [MarineForecastday](docs/MarineForecastday.md)
 - [MarineHour](docs/MarineHour.md)
 - [Search](docs/Search.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## Author



