import requests

class HttpRequester:

    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
        # privado

    def request_from_page(self):
        response = requests.get
        print(response)