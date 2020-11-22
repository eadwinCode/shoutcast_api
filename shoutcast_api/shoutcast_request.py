import xmltodict
import json
from .models import Tunein
from .utils import _init_session
from .Exceptions import APIException

base_url = 'http://api.shoutcast.com'
tunein_url = 'http://yp.shoutcast.com/{base}?id={id}'

tuneins = [Tunein('/sbin/tunein-station.pls'), Tunein('/sbin/tunein-station.m3u'), Tunein('/sbin/tunein-station.xspf')]


def call_api_xml(endpoint, params=None, session=None):
    session = _init_session(session)
    request_url = "{}{}".format(base_url, endpoint)
    response = session.get(request_url, params=params)
    if response.status_code == 200:
        response_as_dict = xmltodict.parse(response.content)
        api_response = response_as_dict.get('response')

        if api_response:
            api_status_code = int(api_response.get('statusCode'))
            message = "statusText:{}, statusDetailText:{}".format(
                api_response.get('statusText'), api_response.get('statusDetailText')
            )
            raise APIException(message, code=api_status_code)

        return response_as_dict
    raise APIException(response.content, code=response.status_code)


def call_api_json(endpoint, params=None, session=None):
    session = _init_session(session)
    request_url = "{}{}".format(base_url, endpoint)
    response = session.get(request_url, params=params)
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))

        api_response = json_response.get('response')
        api_status_code = int(api_response.get('statusCode'))

        if api_status_code != 200:
            message = "statusText:{}, statusDetailText:{}".format(
                api_response.get('statusText'), api_response.get('statusDetailText', '')
            )
            raise APIException(message, code=api_status_code)

        return json_response.get('response')['data']
    raise APIException(response.reason, code=response.status_code)


def call_api_tunein(station_id: int, session=None):
    session = _init_session(session)
    url = tunein_url.format(base=tuneins[2], id=station_id)
    response = session.get(url)
    if response.status_code == 200:
        api_response = xmltodict.parse(response.content.decode('utf-8'))
        return api_response
    raise APIException(response.reason, code=response.status_code)


def call_api_tunein_any(base: Tunein, station_id: int, session=None):
    session = _init_session(session)
    url = tunein_url.format(base=base, id=station_id)
    response = session.get(url)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    raise APIException(response.reason, code=response.status_code)
