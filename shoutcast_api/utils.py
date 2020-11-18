from typing import Tuple


def _build_url(limit: (int, Tuple), **kwargs) -> str:
    url = ""
    if isinstance(limit, tuple):
        x, y = limit
        url += f'&limit={x},{y}'
    elif limit:
        url += f'&limit={limit}'

    if kwargs.get('br'):
        url += f"&br={kwargs.get('br')}"

    if kwargs.get('mt'):
        url += f"&mt={kwargs.get('mt')}"

    if kwargs.get('genre_id'):
        url += f"&genre_id={int(kwargs.get('genre_id'))}"

    if kwargs.get('genre'):
        url += f"&genre={int(kwargs.get('genre'))}"
    return url


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
        genre_ = station.get(f'@genre{i}')
        if not genre_:
            return genre
        genre += f", {genre_}"
    return genre


def _get_all_genre_from_json(station):
    genre = station.get('genre')
    for i in range(2, 10):
        genre_ = station.get(f'genre{i}')
        if not genre_:
            return genre
        genre += f", {genre_}"
    return genre


def genre_xml_strip(genre):
    item = dict()
    item['name'] = genre.get('@name')
    item['count'] = int(genre.get('@count'))
    return item
