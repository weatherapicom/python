# swagger_client.APIsApi

All URIs are relative to *https://api.weatherapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**astronomy**](APIsApi.md#astronomy) | **GET** /astronomy.json | Astronomy API
[**forecast_weather**](APIsApi.md#forecast_weather) | **GET** /forecast.json | Forecast API
[**future_weather**](APIsApi.md#future_weather) | **GET** /future.json | Future API
[**history_weather**](APIsApi.md#history_weather) | **GET** /history.json | History API
[**ip_lookup**](APIsApi.md#ip_lookup) | **GET** /ip.json | IP Lookup API
[**realtime_weather**](APIsApi.md#realtime_weather) | **GET** /current.json | Realtime API
[**search_autocomplete_weather**](APIsApi.md#search_autocomplete_weather) | **GET** /search.json | Search/Autocomplete API
[**time_zone**](APIsApi.md#time_zone) | **GET** /timezone.json | Time Zone API

# **astronomy**
> InlineResponse2003 astronomy(q, dt)

Astronomy API

Return Location and Astronomy Object

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 
 **dt** | **date**| Date on or after 1st Jan, 2015 in yyyy-MM-dd format | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_weather**
> InlineResponse2001 forecast_weather(q, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)

Forecast API

Forecast weather API method returns upto next 10 day weather forecast and weather alert as json. The data is returned as a Forecast Object.   Forecast object contains astronomy data, day weather forecast and hourly interval weather information for a given city. 

### Example
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
days = 56 # int | Number of days of weather forecast. Value ranges from 1 to 14
dt = '2013-10-20' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request. unixdt should be between today and next 14 day in Unix format. e.g. 1490227200  (optional)
hour = 56 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Forecast API
    api_response = api_instance.forecast_weather(q, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->forecast_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 
 **days** | **int**| Number of days of weather forecast. Value ranges from 1 to 14 | 
 **dt** | **date**| Date should be between today and next 14 day in yyyy-MM-dd format. e.g. &#x27;2015-01-01&#x27;  | [optional] 
 **unixdt** | **int**| Please either pass &#x27;dt&#x27; or &#x27;unixdt&#x27; and not both in same request. unixdt should be between today and next 14 day in Unix format. e.g. 1490227200  | [optional] 
 **hour** | **int**| Must be in 24 hour. For example 5 pm should be hour&#x3D;17, 6 am as hour&#x3D;6  | [optional] 
 **lang** | **str**| Returns &#x27;condition:text&#x27; field in API in the desired language.&lt;br /&gt; Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check &#x27;lang-code&#x27;.  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **future_weather**
> InlineResponse2002 future_weather(q, dt=dt, lang=lang)

Future API

Future weather API method returns weather in a 3 hourly interval in future for a date between 14 days and 300 days from today in the future. 

### Example
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
dt = '2013-10-20' # date | Date should be between 14 days and 300 days from today in the future in yyyy-MM-dd format (i.e. dt=2023-01-01)  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Future API
    api_response = api_instance.future_weather(q, dt=dt, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->future_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 
 **dt** | **date**| Date should be between 14 days and 300 days from today in the future in yyyy-MM-dd format (i.e. dt&#x3D;2023-01-01)  | [optional] 
 **lang** | **str**| Returns &#x27;condition:text&#x27; field in API in the desired language.&lt;br /&gt; Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check &#x27;lang-code&#x27;.  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_weather**
> InlineResponse2002 history_weather(q, dt, unixdt=unixdt, end_dt=end_dt, unixend_dt=unixend_dt, hour=hour, lang=lang)

History API

History weather API method returns historical weather for a date on or after 1st Jan, 2010 as json. The data is returned as a Forecast Object. 

### Example
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
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request.<br />unixdt should be on or after 1st Jan, 2015 in Unix format  (optional)
end_dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format<br />'end_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates.  (optional)
unixend_dt = 56 # int | Date on or after 1st Jan, 2015 in Unix Timestamp format<br />unixend_dt has same restriction as 'end_dt' parameter. Please either pass 'end_dt' or 'unixend_dt' and not both in same request. e.g. unixend_dt=1490227200  (optional)
hour = 56 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # History API
    api_response = api_instance.history_weather(q, dt, unixdt=unixdt, end_dt=end_dt, unixend_dt=unixend_dt, hour=hour, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->history_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 
 **dt** | **date**| Date on or after 1st Jan, 2015 in yyyy-MM-dd format | 
 **unixdt** | **int**| Please either pass &#x27;dt&#x27; or &#x27;unixdt&#x27; and not both in same request.&lt;br /&gt;unixdt should be on or after 1st Jan, 2015 in Unix format  | [optional] 
 **end_dt** | **date**| Date on or after 1st Jan, 2015 in yyyy-MM-dd format&lt;br /&gt;&#x27;end_dt&#x27; should be greater than &#x27;dt&#x27; parameter and difference should not be more than 30 days between the two dates.  | [optional] 
 **unixend_dt** | **int**| Date on or after 1st Jan, 2015 in Unix Timestamp format&lt;br /&gt;unixend_dt has same restriction as &#x27;end_dt&#x27; parameter. Please either pass &#x27;end_dt&#x27; or &#x27;unixend_dt&#x27; and not both in same request. e.g. unixend_dt&#x3D;1490227200  | [optional] 
 **hour** | **int**| Must be in 24 hour. For example 5 pm should be hour&#x3D;17, 6 am as hour&#x3D;6  | [optional] 
 **lang** | **str**| Returns &#x27;condition:text&#x27; field in API in the desired language.&lt;br /&gt; Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check &#x27;lang-code&#x27;.  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_lookup**
> Ip ip_lookup(q)

IP Lookup API

IP Lookup API method allows a user to get up to date information for an IP address. 

### Example
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
q = 'q_example' # str | Pass IP address.

try:
    # IP Lookup API
    api_response = api_instance.ip_lookup(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->ip_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass IP address. | 

### Return type

[**Ip**](Ip.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **realtime_weather**
> InlineResponse200 realtime_weather(q, lang=lang)

Realtime API

Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.<br /><br />Current object contains current or realtime weather information for a given city. 

### Example
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
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Realtime API
    api_response = api_instance.realtime_weather(q, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->realtime_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 
 **lang** | **str**| Returns &#x27;condition:text&#x27; field in API in the desired language.&lt;br /&gt; Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check &#x27;lang-code&#x27;.  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_autocomplete_weather**
> ArrayOfSearch search_autocomplete_weather(q)

Search/Autocomplete API

WeatherAPI.com Search or Autocomplete API returns matching cities and towns as an array of Location object. 

### Example
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

try:
    # Search/Autocomplete API
    api_response = api_instance.search_autocomplete_weather(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->search_autocomplete_weather: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 

### Return type

[**ArrayOfSearch**](ArrayOfSearch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_zone**
> Location time_zone(q)

Time Zone API

Return Location Object

### Example
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

try:
    # Time Zone API
    api_response = api_instance.time_zone(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->time_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.  | 

### Return type

[**Location**](Location.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

