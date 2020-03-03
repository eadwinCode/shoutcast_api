from typing import List


class Station:
    def __init__(self, station):
        self.name = station.get('name')
        self.id = station.get('id')
        self.br = station.get('br')
        self.genre = station.get('genre')
        self.ct = station.get('ct')
        self.mt = station.get('mt')
        self.lc = int(station.get('lc'))
        self.logo_url = station.get('logo')

    def __str__(self):
        return self.name


class Tunein:
    def __init__(self, tunein):
        self.path = tunein

    def __str__(self):
        return self.path


class StationList:
    def __init__(self, stations: List[Station], tunein: List[Tunein]):
        self.station = stations
        self.tunein = tunein


class Genre:
    def __init__(self, genre):
        self.name = genre.get('name')
        self.id = genre.get('id')
        self.count = genre.get('count')
        self.haschildren = genre.get('haschildren')
        self.parentid = genre.get('parentid')
        self.genrelist = self.get_genre_list(genre)

    def __str__(self):
        return self.name

    @classmethod
    def get_genre_list(cls, genre):
        output = []
        genre_list = genre.get('genrelist')
        if not genre_list:
            return genre_list

        for item in genre_list.get('genre', list()):
            output.append(Genre(item))
        return output


class GenreList:
    def __init__(self, genres: List[Genre]):
        self.genres = genres


class Track:
    def __init__(self, track):
        self.stream_url = track.get('location')
        self.title = track.get('title')


class TrackList:
    def __init__(self, tracks: List[Track]):
        self.tracks = tracks
