# coding: utf-8

"""
    Weather API

    # Introduction WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy. We provide following data through our API:     - Real-time weather - 14 day weather forecast - Historical Weather - Marine Weather and Tide Data - Future Weather (Upto 365 days ahead) - Daily and hourly intervals - 15 min interval (Enterprise only) - Astronomy - Time zone - Location data - Sports - Search or Autocomplete API - Weather Alerts - Air Quality Data - Bulk Request  # Getting Started    You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!  Try our weather API by using interactive [API Explorer](https://www.weatherapi.com/api-explorer.aspx).  We also have SDK for popular framework/languages available on [Github](https://github.com/weatherapicom/) for quick integrations.  If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).    # Authentication    API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.    Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .      ##  key parameter  key=YOUR API KEY    # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from weatherapi.configuration import Configuration


class MarineForecastday(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_date': 'date',
        'date_epoch': 'int',
        'day': 'ForecastDay',
        'astro': 'ForecastAstro',
        'hour': 'list[MarineHour]'
    }

    attribute_map = {
        '_date': 'date',
        'date_epoch': 'date_epoch',
        'day': 'day',
        'astro': 'astro',
        'hour': 'hour'
    }

    def __init__(self, _date=None, date_epoch=None, day=None, astro=None, hour=None, _configuration=None):  # noqa: E501
        """MarineForecastday - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._date_epoch = None
        self._day = None
        self._astro = None
        self._hour = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if date_epoch is not None:
            self.date_epoch = date_epoch
        if day is not None:
            self.day = day
        if astro is not None:
            self.astro = astro
        if hour is not None:
            self.hour = hour

    @property
    def _date(self):
        """Gets the _date of this MarineForecastday.  # noqa: E501


        :return: The _date of this MarineForecastday.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MarineForecastday.


        :param _date: The _date of this MarineForecastday.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def date_epoch(self):
        """Gets the date_epoch of this MarineForecastday.  # noqa: E501


        :return: The date_epoch of this MarineForecastday.  # noqa: E501
        :rtype: int
        """
        return self._date_epoch

    @date_epoch.setter
    def date_epoch(self, date_epoch):
        """Sets the date_epoch of this MarineForecastday.


        :param date_epoch: The date_epoch of this MarineForecastday.  # noqa: E501
        :type: int
        """

        self._date_epoch = date_epoch

    @property
    def day(self):
        """Gets the day of this MarineForecastday.  # noqa: E501


        :return: The day of this MarineForecastday.  # noqa: E501
        :rtype: ForecastDay
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this MarineForecastday.


        :param day: The day of this MarineForecastday.  # noqa: E501
        :type: ForecastDay
        """

        self._day = day

    @property
    def astro(self):
        """Gets the astro of this MarineForecastday.  # noqa: E501


        :return: The astro of this MarineForecastday.  # noqa: E501
        :rtype: ForecastAstro
        """
        return self._astro

    @astro.setter
    def astro(self, astro):
        """Sets the astro of this MarineForecastday.


        :param astro: The astro of this MarineForecastday.  # noqa: E501
        :type: ForecastAstro
        """

        self._astro = astro

    @property
    def hour(self):
        """Gets the hour of this MarineForecastday.  # noqa: E501


        :return: The hour of this MarineForecastday.  # noqa: E501
        :rtype: list[MarineHour]
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this MarineForecastday.


        :param hour: The hour of this MarineForecastday.  # noqa: E501
        :type: list[MarineHour]
        """

        self._hour = hour

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MarineForecastday, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarineForecastday):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarineForecastday):
            return True

        return self.to_dict() != other.to_dict()
