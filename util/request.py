from requests import get
from json import loads


class Api(object):
    """ Api representa uma API da qual iremos consumir informações.

    Args:
        url: URL da API.
    """
    def __init__(self, url: str) -> None:
        self.__url = url

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        self.__url = url

    def get_data(self) -> dict:
        res = get(self.url)
        if res.status_code == 200:
            data = res.text
            return loads(data)
        return None

