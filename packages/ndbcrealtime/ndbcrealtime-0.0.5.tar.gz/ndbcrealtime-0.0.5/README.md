# NOAA NDBC-API (ndbcrealtime)
PyPi Integration to the NOAA National Data Buoy Centre real time observations for wind, waves, sea level pressure, air temperature, water temperature, dewpoint, visibility, pressure tendency, and tide information (as available) for a specific buoy.

## Available Classes and Methods

### Class NDBC(station_id, session (optional))

Create an instance of the NDBC class with a specific station_id in order to retrieve the current observation data using `get_data()`

**station_id (string):** the station id for the buoy which can be found from the NDBC website: https://www.ndbc.noaa.gov/

Session can be sent as an optional aiohttp session if you are managing your session within an application.

#### get_data()

Returns the current observation data as a JSON object.

**Return Payload**

The payload returned will be structured as:

```json
{
    "location": {
        "latitude": latitude (float),
        "longitude": longitude (float),
        "elevation": elevation (int),
        "name": station name (str)
    },
    "observation": {
        "time": {
            "utc_time": utc date/time (datetime),
            "unix_time": unix timestamp (int)
        },
        "wind": {
            "direction": wind direction (int),
            "direction_unit": direction units (str),
            "direction_compass": direction text (str),
            "speed": wind speed (float),
            "speed_unit": speed units (str),
            "gusts": wind gusts (float),
            "gusts_unit": gusts units (str)
        },
        "waves": {
            "height": wave height (float),
            "height_unit": wave height units (str),
            "period": dominant wave period (int),
            "period_unit": wave period units (str),
            "average_period": average wave period (int),
            "average_period_unit": average period units (str),
            "direction": dominant wave direction (int),
            "direction_unit": dominant direction units (str),
            "direction_compass": direction text (str)
        },
        "weather": {
            "pressure": sea level pressure (float),
            "pressure_unit": pressure units (str),
            "air_temperature": air temperature (float),
            "air_temperature_unit": air temperature units (str),
            "water_temperature": water temperature (float),
            "water_temperature_unit": water temperature units (str),
            "dewpoint": dewpoint temperature (float),
            "dewpoint_unit": dewpoint_units (str),
            "visibility": visibility (float),
            "visibility_unit": visibility units (str),
            "pressure_tendency": pressure tendency (float),
            "pressure_tendency_unit": pressure tendency units (str),
            "tide": tide (float),
            "tide_unit": tide units (float)
        }
    }
}
```

### Class Stations()

Create an instance of the Stations class to retrieve a list of available stations from the NDBC database.

#### list()

Returns a dict containing all available NDBC stations.

**Return Payload**

The payload returned will be structured as:

```json
{
    '00922': {
        '@id': '00922', 
        '@lat': '30', 
        '@lon': '-90', 
        '@name': 'OTN201 - 4800922', 
        '@owner': 'Dalhousie University', 
        '@pgm': 'IOOS Partners', 
        '@type': 'other', 
        '@met': 'n', 
        '@currents': 'n', 
        '@waterquality': 'n', 
        '@dart': 'n'},
    ...
}
```

Note: This library was built specifically for integration to Home Assistant.
