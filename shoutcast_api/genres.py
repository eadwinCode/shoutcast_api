from shoutcast_api import shoutcast_request
from typing import Tuple, AnyStr, List
from .models import Genre, GenreList
from .utils import _build_url, genre_xml_strip


def _handle_url_action_json(url):
    list_genre: List[Genre] = []
    response = shoutcast_request.call_api_json(url)

    genrelist = response.get('genrelist')

    if not genrelist.get('genre'):
        return GenreList(list_genre)

    for item in genrelist.get('genre'):
        list_genre.append(Genre(item))
    return GenreList(list_genre)


def get_all_genres(api_key):
    """
    Get all the genres on SHOUTcast Radio Directory
    :param api_key: API Dev ID
    :return: `class GenreList()`
    """
    list_genre: List[Genre] = []
    url = f"legacy/genrelist?k={api_key}"
    response = shoutcast_request.call_api_xml(url)

    genrelist = response.get('genrelist')

    if not genrelist or not genrelist.get('genre'):
        return GenreList(list_genre)

    for item in genrelist.get('genre'):
        list_genre.append(Genre(genre_xml_strip(item)))
    return GenreList(list_genre)


def get_primary_genres_json(api_key):
    """
    Get only the Primary Genres on SHOUTcast Radio Directory
    :param api_key: API Dev ID
    :return: `class GenreList()`
    """

    url = f"genre/primary?k={api_key}&f=json"

    return _handle_url_action_json(url)


def get_secondary_genres_json(api_key, parentid: int = 0):
    """
    Get secondary genre list (if present) for a specified primary genre.
    :param parentid: Genreid of the primary genre. You can retrieve the entire genre set by passing parentid=0.
    :param api_key: API Dev ID
    :return: `class GenreList()`
    """

    url = f"genre/secondary?k={api_key}&f=json"
    url += f"&parentid={parentid}"
    return _handle_url_action_json(url)


def get_genres_details_by_id(api_key, genre_id: int = None) -> Genre:
    """
    Get details such as Genre Name, Sub Genres (if its a primary genre), has children by passing the genre-id.
    :param genre_id: Input respective genre or sub-genre id.
    :param api_key: API Dev ID
    :return: `class GenreList()`
    """
    if not genre_id:
        raise Exception('id is required')

    url = f"genre/secondary?k={api_key}&f=json&id={genre_id}"
    response = shoutcast_request.call_api_json(url)

    genrelist = response.get('genrelist')

    if not genrelist.get('genre'):
        return Genre({})

    return Genre(genrelist.get('genre'))


def get_genres_by_sub_genres(api_key, haschildren: bool = False):
    """
    Get genres based on their sub-genre availability at any node level in the genre hierarchy of SHOUTcast.
    :param haschildren: Input respective genre or sub-genre id.
        'true' to get genre or subgenre which has sub-genres.
        'false' to get genre or subgenre which does not have sub-genres.

    :param api_key: API Dev ID
    :return: `class GenreList()`
    """

    url = f"genre/secondary?k={api_key}&f=json"
    if haschildren:
        url += '&haschildren=true'
    else:
        url += '&haschildren=false'

    return _handle_url_action_json(url)
