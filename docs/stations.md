## `Stations` module
All functions that returns `stationslist` are groups under this module.

Usage:
```python
from shoutcast_api import stations
```

#### `get_top_500`
Gets top 500 stations from shoutcast api.

Params:
```k: str - API Dev Key.
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_top_500(k, limit=100)
```

#### `get_stations_keywords`
 Get stations which match the keyword searched on SHOUTcast Radio Directory.

Params:
```k: str - API Dev Key.
   search: str - search query.
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_stations_keywords(k, search='Hot', limit=100, br=128)
```

#### `get_stations_by_genre`
 Get stations which match the genre specified as query.

Params:
```k: str - API Dev Key.
   genre: str - genre name
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_stations_by_genre(k, genre='Hip Hop', limit=100, br=128)
```


#### `get_stations_by_now_playing`
 Return stations which match a specified query in the now playing node. 

Params:
```k: str - API Dev Key.
   ct: str - Query to search in Now Playing node. This parameter also supports querying multiple artists in the same query by using "||". ex: ct=madonna||u2||beyonce up to 10 artists 
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_stations_by_now_playing(k, ct='john legend', limit=100, br=128)
```

#### `get_stations_bitrate_or_genre_id`
  Get stations which match the genre specified as query.

Params:
```k: str - API Dev Key.
   genre_id: int - genre id
   ct: str - Query to search in Now Playing node. This parameter also supports querying multiple artists in the same query by using "||". ex: ct=madonna||u2||beyonce up to 10 artists 
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_stations_bitrate_or_genre_id(k, limit=100, br=128, genre_id=25)
```

#### `get_random_station`
 Get random stations on SHOUTcast Radio Directory. Random stations can be restricted to the Bitrate/Genre/Media type specified.

Params:
```k: str - API Dev Key.
   genre_id: int - genre id
   ct: str - Query to search in Now Playing node. This parameter also supports querying multiple artists in the same query by using "||". ex: ct=madonna||u2||beyonce up to 10 artists 
   limit: int or tuple(X,Y) - limit the number of stations to return by passing the limit parameter. for example `limit=(X,Y)` - Y is the number of results to return and X is the offset.
   br: int - Filter the stations based on bitrate specified.
   mt: str - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
```

Usage:
```python
  response = stations.get_random_station(k, limit=100)
```



### Response object field definitions

#### `Station`

```
name : str - station name
id : int - station id
genre : str - station genre tags
br : int - station bitrate
ct : str - station current playing info
logo_url : str - station logo
lc : str
```

#### `Tunein`

```
path : str
```

#### `StationList`

```
station : List[Genre] array of Station
tunein: List[Tunein] array of Tunein
```