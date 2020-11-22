from shoutcast_api import shoutcast_request
from .models import Genre, GenreList
from .utils import genre_xml_strip


def _handle_url_action_json(endpoint, params, session):
    list_genre = []
    response = shoutcast_request.call_api_json(endpoint, params=params, session=session)

    genrelist = response.get('genrelist')

    if not genrelist.get('genre'):
        return GenreList(list_genre)

    for item in genrelist.get('genre'):
        list_genre.append(Genre(item))
    return GenreList(list_genre)


def get_all_genres(k, session=None):
    """
    Get all the genres on SHOUTcast Radio Directory
    :param k: API Dev ID
    :param session: request_cache session if available
    :return: `class GenreList()`
    """
    list_genre = []
    endpoint = "/legacy/genrelist"
    params = dict(k=k)
    response = shoutcast_request.call_api_xml(endpoint, session=session, params=params)

    genrelist = response.get('genrelist')

    if not genrelist or not genrelist.get('genre'):
        return GenreList(list_genre)

    for item in genrelist.get('genre'):
        list_genre.append(Genre(genre_xml_strip(item)))
    return GenreList(list_genre)


def get_primary_genres_json(k, session=None):
    """
    Get only the Primary Genres on SHOUTcast Radio Directory
    :param k: API Dev ID
    :param session: request_cache session if available
    :return: `class GenreList()`
    """

    endpoint = "/genre/primary"
    params = dict(k=k, f='json')
    return _handle_url_action_json(endpoint, session=session, params=params)


def get_secondary_genres_json(k, parentid: int = 0, session=None):
    """
    Get secondary genre list (if present) for a specified primary genre.
    :param parentid: Genreid of the primary genre. You can retrieve the entire genre set by passing parentid=0.
    :param k: API Dev ID
    :param session: request_cache session if available
    :return: `class GenreList()`
    """

    endpoint = "/genre/secondary".format(k)
    params = dict(k=k, f='json', parentid=str(parentid))
    return _handle_url_action_json(endpoint, session=session, params=params)


def get_genres_details_by_id(k, genre_id: int = None, session=None) -> Genre:
    """
    Get details such as Genre Name, Sub Genres (if its a primary genre), has children by passing the genre-id.
    :param genre_id: Input respective genre or sub-genre id.
    :param k: API Dev ID
    :param session: request_cache session if available
    :return: `class GenreList()`
    """
    if not genre_id:
        raise Exception('id is required')

    endpoint = "/genre/secondary"
    params = dict(k=k, id=str(genre_id), f='json')
    response = shoutcast_request.call_api_json(endpoint, params=params, session=session)

    genrelist = response.get('genrelist')

    if not genrelist.get('genre'):
        return Genre({})

    return Genre(genrelist.get('genre'))


def get_genres_by_sub_genres(k, haschildren: bool = False, session=None):
    """
    Get genres based on their sub-genre availability at any node level in the genre hierarchy of SHOUTcast.
    :param haschildren: Input respective genre or sub-genre id.
        'true' to get genre or subgenre which has sub-genres.
        'false' to get genre or subgenre which does not have sub-genres.

    :param k: API Dev ID
    :param session: request_cache session if available
    :return: `class GenreList()`
    """

    endpoint = "/genre/secondary"
    params = dict(k=k, f='json')
    if haschildren:
        params.update(haschildren=True)
    else:
        params.update(haschildren=False)

    return _handle_url_action_json(endpoint, params=params, session=session)
