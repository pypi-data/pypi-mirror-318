from bs4 import BeautifulSoup
import requests

class response_object(requests.Response):
    def __init__(self, url):
        super().__init__()
        self.charset = 'utf-8'
        self.text_ = requests.get(url).text
    def set_charset(self, charset):
        self.charset = charset
    def get(self,get_type):
        soup = BeautifulSoup(self.text_, 'html.parser')
        all_get = soup.find_all(get_type)
        return all_get

def crawl(url):
    response = requests.get(url)
    if response.status_code == 200:
        response = response_object(url)
        return response
    else:
        print(f"Could not crawl the page. Status code: {response.status_code}")
        return None