## `Tunein` module
All functions on how to Tune Into A Station are grouped under this module.

Usage:
```python
from shoutcast_api import tunein
```

#### `get_stations_stream_url`
Gets the stations streaming urls as TrackList

Params:
```
station_id: int - Station id
```
Usage:
```python
 response = tunein.get_stations_stream_url(station_id)
```

#### `tunein_to_station`
Get station tunein detail in format provided as `base` param

Params:
```
station_id: int - Station id
base: Tunein - value is taken from the tunein node and based on the playlist format required
    (as PLS, M3U and XSPF formats are supported)
```
Usage:
```python
 response = tunein.tunein_to_station(base, station_id)
```

### Response object field definitions

#### `Track`

```
title : str - station name
stream_url : str - streaming url
```


#### `TrackList`

```
tracks : List[Track] array of Track
```