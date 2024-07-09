# coding: utf-8

"""
    Weather API

     # Introduction  WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy.      We provide following data through our API:      - Real-time weather  - 14 day weather forecast  - Astronomy  - Time zone  - Location data  - Search or Autocomplete API  - NEW: Historical weather  - NEW: Future Weather (Upto 300 days ahead)  - Weather Alerts  - Air Quality Data    # Getting Started     You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!      We have [code libraries](https://www.weatherapi.com/docs/code-libraries.aspx) for different programming languages like PHP, .net, JAVA, etc.  If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).      # Authentication     API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.  Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .        ##  key parameter   key=YOUR_API_KEY   # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import weatherapi
from weatherapi.api.ap_is_api import APIsApi  # noqa: E501
from weatherapi.rest import ApiException


class TestAPIsApi(unittest.TestCase):
    """APIsApi unit test stubs"""

    def setUp(self):
        self.api = APIsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_astronomy(self):
        """Test case for astronomy

        Astronomy API  # noqa: E501
        """
        pass

    def test_forecast_weather(self):
        """Test case for forecast_weather

        Forecast API  # noqa: E501
        """
        pass

    def test_future_weather(self):
        """Test case for future_weather

        Future API  # noqa: E501
        """
        pass

    def test_history_weather(self):
        """Test case for history_weather

        History API  # noqa: E501
        """
        pass

    def test_ip_lookup(self):
        """Test case for ip_lookup

        IP Lookup API  # noqa: E501
        """
        pass

    def test_realtime_weather(self):
        """Test case for realtime_weather

        Realtime API  # noqa: E501
        """
        pass

    def test_search_autocomplete_weather(self):
        """Test case for search_autocomplete_weather

        Search/Autocomplete API  # noqa: E501
        """
        pass

    def test_time_zone(self):
        """Test case for time_zone

        Time Zone API  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
