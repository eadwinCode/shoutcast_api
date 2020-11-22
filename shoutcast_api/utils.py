import requests
from typing import Tuple


def _build_url(limit: (int, Tuple), **kwargs) -> dict:
    url_params = dict()
    if isinstance(limit, tuple):
        x, y = limit
        url_params.update(limit='{},{}'.format(x, y))
    elif limit:
        url_params.update(limit=str(limit))

    if kwargs.get('br'):
        url_params.update(br=kwargs.get('br'))

    if kwargs.get('mt'):
        url_params.update(mt=kwargs.get('mt'))

    if kwargs.get('genre_id'):
        url_params.update(genre_id=kwargs.get('genre_id'))

    if kwargs.get('genre'):
        url_params.update(genre=kwargs.get('genre'))
    return url_params


def station_xml_strip(station):
    item = dict()
    item['name'] = station.get('@name')
    item['id'] = int(station.get('@id'))
    item['br'] = int(station.get('@br'))
    item['genre'] = _get_all_genre(station)
    item['ct'] = station.get('@ct')
    item['lc'] = int(station.get('@lc'))
    item['logo'] = station.get('@logo')
    item['mt'] = station.get('@mt')
    return item


def station_json_strip(station):
    item = dict()
    item.update(**station)
    item['genre'] = _get_all_genre_from_json(station)
    return item


def _get_all_genre(station):
    genre = station.get('@genre')
    for i in range(2, 10):
        genre_ = station.get('@genre{}'.format(i))
        if not genre_:
            return genre
        genre += ", {}".format(genre_)
    return genre


def _get_all_genre_from_json(station):
    genre = station.get('genre')
    for i in range(2, 10):
        genre_ = station.get('genre{}'.format(i))
        if not genre_:
            return genre
        genre += ", {}".format(genre_)
    return genre


def genre_xml_strip(genre):
    item = dict()
    item['name'] = genre.get('@name')
    item['count'] = int(genre.get('@count'))
    return item


def _init_session(session):
    if session is None:
        session = requests.Session()
    return session
