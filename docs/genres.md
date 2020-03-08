## `Genres` module
All functions that returns `genrelist` or `genre` are groups under this module.

Usage:
```python
from shoutcast_api import genres
```

#### `get_all_genres`
Get all the genres on SHOUTcast Radio Directory

Params:
```
k: str - API Dev Key
```
Usage:
```python
 response = genres.get_all_genres(k)
```

#### `get_primary_genres_json`
Get only the Primary Genres on SHOUTcast Radio Directory.

Params:
```
k: str - API Dev Key
```
Usage:
```python
 response = genres.get_primary_genres_json(k)
```

#### `get_secondary_genres_json`
Get secondary genre list (if present) for a specified primary genre.

Params:
```
k: str - API Dev Key
parent_id: int -  Genreid of the primary genre. You can retrieve the entire genre set by passing parentid=0.
```
Usage:
```python
 response = genres.get_secondary_genres_json(k, parent_id=1)
```

#### `get_genres_details_by_id`
Get details such as Genre Name, Sub Genres (if its a primary genre), has children by passing the genre-id.

Params:
```
k: str - API Dev Key
genre_id: int -  Input respective genre or sub-genre id.
```
Usage:
```python
 response = genres.get_genres_details_by_id(k, genre_id=25)
```

#### `get_genres_by_sub_genres`
Get details such as Genre Name, Sub Genres (if its a primary genre), has children by passing the genre-id.

Params:
```
k: str - API Dev Key
haschildren: bool -  
'true' to get genre or subgenre which has sub-genres.
'false' to get genre or subgenre which does not have sub-genres.
```
Usage:
```python
 response = genres.get_genres_by_sub_genres(k, genre_id=25)
```

### Response object field definitions

#### `Genre`

```
name : str - genre name
id : int - genre id
count : int - stations count
haschildren : str
parentid : int - genre parent id
genrelist : List[Genre] array of children genre if haschildren is true
```


#### `GenreList`

```
genres : List[Genre] array of Genre
```