import requests
from bs4 import BeautifulSoup


class Parser(object):
    parser = None #Singleton object

    def __new__(cls):
        if cls.parser is None:
            cls.parser = object.__new__(cls)
        return cls.parser
    
    @property
    def set_url(self, url):
        self._url = url
    
    def parse(self, url):
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


parser = Parser()
parser.parse('https://docs.python.org/3/whatsnew/3.13.html')

        
    