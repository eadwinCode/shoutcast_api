from shoutcast_api import shoutcast_request
from typing import Tuple, AnyStr, List
from .models import Station, StationList
from .utils import _build_url, station_xml_strip, station_json_strip


def _handle_url_action_xml(url: str):
    stations: List[Station] = list()
    response = shoutcast_request.call_api_xml(url)
    api_station_list = response.get('stationlist')

    if not api_station_list.get('station'):
        return StationList(tunein=shoutcast_request.tuneins, stations=[])

    api_stations = api_station_list.get('station')
    if not isinstance(api_stations, list):
        return StationList(tunein=shoutcast_request.tuneins, stations=[Station(station_xml_strip(api_stations))])

    for item in api_stations:
        stations.append(Station(station_xml_strip(item)))

    return StationList(tunein=shoutcast_request.tuneins, stations=stations)


def _handle_url_action_json(url: str) -> StationList:
    stations: List[Station] = list()
    response = shoutcast_request.call_api_json(url)
    api_station_list = response.get('stationlist')

    if not api_station_list.get('station'):
        return StationList(tunein=shoutcast_request.tuneins, stations=[])

    api_stations = api_station_list.get('station')
    if not isinstance(api_stations, list):
        return StationList(tunein=shoutcast_request.tuneins, stations=[Station(station_json_strip(api_stations))])

    for item in api_stations:
        stations.append(Station(station_json_strip(item)))

    return StationList(tunein=shoutcast_request.tuneins, stations=stations)


def get_top_500(api_key: AnyStr, limit: (int, Tuple) = None, **kwargs) -> StationList:
    """
    gets top 500 stations from shoutcast api
    :param api_key: API Dev Key.
    :param limit: limit the number of stations to return by passing the limit parameter. for example
    `limit=(X,Y)` - Y is the number of results to return and X is the offset.
    :param kwargs:
        br - Filter the stations based on bitrate specified.
        mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
    :return: list of stations
    """

    url = f'/legacy/Top500?k={api_key}'
    url += _build_url(limit=limit, **kwargs)

    return _handle_url_action_xml(url)


def get_stations_keywords(api_key, search: str, limit: (int, Tuple) = None, **kwargs) -> StationList:
    """
        Get stations which match the keyword searched on SHOUTcast Radio Directory.
       :param search: Specify the query to search
       :param api_key: API Dev Key.
       :param limit: limit the number of stations to return by passing the limit parameter. for example
       `limit=(X,Y)` - Y is the number of results to return and X is the offset.
       :param kwargs:
           br - Filter the stations based on bitrate specified.
           mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
       :return: `List[Stations]`
    """
    if not search:
        raise Exception('Search query is required')

    url = f"legacy/stationsearch?k={api_key}&search={search.replace(' ', '+').strip()}"
    url += _build_url(limit, **kwargs)

    return _handle_url_action_xml(url)


def get_stations_by_genre(api_key, genre: str, limit: (int, Tuple) = None, **kwargs) -> StationList:
    """
       Get stations which match the genre specified as query.
       :param genre: genre
       :param api_key: API Dev Key.
       :param limit: limit the number of stations to return by passing the limit parameter. for example
      `limit=(X,Y)` - Y is the number of results to return and X is the offset.
       :param kwargs:
           br - Filter the stations based on bitrate specified.
           mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
       :return: `List[Stations]`
    """
    if not genre:
        raise Exception('genre is required')

    url = f"legacy/stationsearch?k={api_key}&search={genre.replace(' ', '+').strip()}"
    url += _build_url(limit, **kwargs)

    return _handle_url_action_xml(url)


def get_stations_by_now_playing(api_key, ct: str, limit: (int, Tuple) = None, **kwargs) -> StationList:
    """
       Return stations which match a specified query in the now playing node.
       :param ct: Query to search in Now Playing node. This parameter also supports querying multiple artists in the same query by using "||". ex: ct=madonna||u2||beyonce up to 10 artists
       :param api_key: API Dev Key.
       :param limit: limit the number of stations to return by passing the limit parameter. for example
       `limit=(X,Y)` - Y is the number of results to return and X is the offset.
       :param kwargs:
           br - Filter the stations based on bitrate specified.
           mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
       :return: `List[Stations]`
    """
    if not ct:
        raise Exception('genre is required')

    url = f"station/nowplaying?k={api_key}&ct={ct.replace(' ', '+').strip()}&f=json"
    url += _build_url(limit, **kwargs)

    return _handle_url_action_json(url)


def get_stations_bitrate_or_genre_id(api_key, br: int = 128,
                                     genre_id: int = None, limit: (int, Tuple) = None, **kwargs) -> StationList:
    """
          Get stations which match the genre specified as query.
          :param genre_id: genre id
          :param br: bitrate
          :param api_key: API Dev Key.
          :param limit: limit the number of stations to return by passing the limit parameter. for example
          `limit=(X,Y)` - Y is the number of results to return and X is the offset.
          :param kwargs:
              mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
          :return: `List[Stations]`
       """

    if not br and not genre_id:
        raise Exception('genre_id or br is required')

    url = f"station/advancedsearch?k={api_key}&f=json"
    url += _build_url(limit, br=br, genre_id=genre_id, **kwargs)

    return _handle_url_action_json(url)


def get_random_station(api_key, limit: (int, Tuple) = None, **kwargs):
    """
          Get random stations on SHOUTcast Radio Directory. Random stations can be restricted
          to the Bitrate/Genre/Media type specified.
          :param api_key: API Dev Key.
          :param limit: limit the number of stations to return by passing the limit parameter. for example
          `limit=(X,Y)` - Y is the number of results to return and X is the offset.
          :param kwargs:
              br - Filter the stations based on bitrate specified.
              mt - Filter the stations based on media type specified, MP3 = audio/mpeg and AAC+ = audio/aacp
              genre - Genre to filter the station result.
          :return: `List[Stations]`
       """

    url = f"station/randomstations?k={api_key}&f=json"
    url += _build_url(limit, **kwargs)

    return _handle_url_action_json(url)
