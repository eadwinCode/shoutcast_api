# Shoutcast Radio Directory API

A Python module for interacting with the shoutcast radio directory api. For Python >= 3.

### Getting started

Installation via pip:

```
$ pip install shoutcast-api
```

Manual installation:
```
$ git clone https://github.com/eadwinCode/shoutcast_api
$ cd shoutcast_api
$ python setup.py install
```

The module consists of the following sub-modules:

* `stations` ([docs](docs/stations.md))
* `genres` ([docs](docs/genres.md)) 

Usage:
```python
from shoutcast_api import get_stations_by_now_playing
response = stations.get_stations_by_now_playing(api_key, ct='john legend', limit=100, br=128)
```

### Error handling

All functions may raise exceptions if incorrect parameters are passed or other problems. If it is server-error `APIException` exception will be raised.


### SHOUTcast API Usage Restrictions

By using our API, you agree to the following restrictions which are in place to protect the SHOUTcast brand and ServiceMark.

- Please do not hammer the servers. We request reasonable usage and recommend that you utilize local caching.
- Do not copy the shoutcast.com design, make your design as original as possible.
- We reserve the right to revoke access for DevIDs which abuse the system.
- We have included official logos for your usage below (with more to follow later).


### API License Terms
For License Terms, [here](https://shoutcast.com/Legal/LicenseAPI) 